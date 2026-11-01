import difflib
import os
import time
import pandas as pd
from spotify_scraper import SpotifyClient

files = [
    "angry.csv",
    "disgusted.csv",
    "fearful.csv",
    "happy.csv",
    "neutral.csv",
    "sad.csv",
    "surprised.csv"
]

with SpotifyClient() as client:

    for filename in files:
        path = os.path.join("songs", filename)

        print(f"\nProcessing {filename}...")
        df = pd.read_csv(path)

        if "Spotify_Link" not in df.columns:
            df["Spotify_Link"] = ""

        for index, row in df.iterrows():

            if pd.notna(row["Spotify_Link"]) and row["Spotify_Link"]:
                continue

            query = f'{row["Name"]} {row["Artist"]}'

            try:
                results = client.search(
                    query,
                    types=("track",),
                    limit=5
                )

                tracks = results.tracks

                if tracks:
                    def similarity(track):
                        data = track.to_dict()

                        title_score = difflib.SequenceMatcher(
                            None,
                            str(row["Name"]).lower(),
                            str(data.get("name", "")).lower()
                        ).ratio()

                        artists = " ".join(
                            artist["name"] for artist in data.get("artists", [])
                        ).lower()

                        artist_score = difflib.SequenceMatcher(
                            None,
                            str(row["Artist"]).lower(),
                            artists
                        ).ratio()

                        return title_score * 0.7 + artist_score * 0.3

                    best_track = max(tracks, key=similarity)
                    best = best_track.to_dict()
                    uri = best.get("uri", "")

                    if uri.startswith("spotify:track:"):
                        track_id = uri.split(":")[-1]
                        df.at[index, "Spotify_Link"] = (
                            f"https://open.spotify.com/track/{track_id}"
                        )

                        print(f"Found: {row['Name']}")
                    else:
                        print(f"No valid link: {row['Name']}")
                else:
                    print(f"Not found: {row['Name']}")

            except Exception as error:
                print(f"Error for {row['Name']}: {error}")

            time.sleep(1)

        df.to_csv(path, index=False)
        print(f"Saved: {filename}")

print("\nAll playlists processed!")
