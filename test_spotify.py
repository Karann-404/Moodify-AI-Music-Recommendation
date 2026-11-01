
from spotify_scraper import SpotifyClient

with SpotifyClient() as client:
    results = client.search(
        "Fearless Pt. II",
        types=("track",),
        limit=5
    )

    for track in results.tracks:
        data = track.to_dict()

        artists = ", ".join(
            artist["name"] for artist in data.get("artists", [])
        )

        print("Song:", data.get("name"))
        print("Artist:", artists)
        print("Spotify URI:", data.get("uri"))
        print("-" * 40)
