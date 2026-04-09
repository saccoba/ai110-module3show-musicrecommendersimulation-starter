"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs, UserProfile, Recommender, Song


def main() -> None:
    songs_dicts = load_songs("data/songs.csv")
    songs = [
        Song(
            id=int(song['id']),
            title=song['title'],
            artist=song['artist'],
            genre=song['genre'],
            mood=song['mood'],
            energy=float(song['energy']),
            tempo_bpm=float(song['tempo_bpm']),
            valence=float(song['valence']),
            danceability=float(song['danceability']),
            acousticness=float(song['acousticness'])
        )
        for song in songs_dicts
    ] 

    # Define a specific taste profile
    user_profile = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        likes_acoustic=False
    )

    # Use the OOP recommender
    recommender = Recommender(songs)
    recommendations = recommender.recommend(user_profile, k=5)

    print("\n🎵 Top Music Recommendations 🎵\n")
    print("-" * 50)
    
    for i, song in enumerate(recommendations, 1):
        # Calculate score (replicating the logic from recommend method)
        genre_score = 1.0 if song.genre == user_profile.favorite_genre else 0.0
        mood_score = 1.0 if song.mood == user_profile.favorite_mood else 0.0
        energy_score = 1.0 - abs(song.energy - user_profile.target_energy)
        acoustic_score = song.acousticness if user_profile.likes_acoustic else (1.0 - song.acousticness)
        total_score = genre_score + mood_score + energy_score + acoustic_score
        
        explanation = recommender.explain_recommendation(user_profile, song)
        
        print(f"{i}. {song.title}")
        print(f"   by {song.artist}")
        print(f"   Score: {total_score:.2f}/4.00")
        print(f"   {explanation}")
        print()


if __name__ == "__main__":
    main()
