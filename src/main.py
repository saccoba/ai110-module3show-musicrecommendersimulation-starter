"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs_dicts = load_songs("data/songs.csv")

    # Define distinct user preference dictionaries
    user_profiles = {
        "High-Energy Pop": {"genre": "pop", "mood": "happy", "energy": 0.9},
        "Chill Lofi": {"genre": "lofi", "mood": "chill", "energy": 0.3},
        "Deep Intense Rock": {"genre": "rock", "mood": "intense", "energy": 0.95}
    }

    # Run recommendations for each profile
    for profile_name, user_prefs in user_profiles.items():
        print(f"\n🎵 Top recommendations for {profile_name} 🎵\n")
        print("-" * 50)
        
        recommendations = recommend_songs(user_prefs, songs_dicts, k=5)
        
        for rec in recommendations:
            song, score, explanation = rec
            print(f"{song['title']} by {song['artist']} - Score: {score:.2f}")
            print(f"Because: {explanation}")
            print()


if __name__ == "__main__":
    main()
