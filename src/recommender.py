from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """
        Recommend songs based on user profile.
        
        Algorithm:
        1. Score each song based on match to user preferences:
           - Genre: 1.0 if exact match, 0.0 otherwise
           - Mood: 1.0 if exact match, 0.0 otherwise  
           - Energy: 1 - |song.energy - user.target_energy| (closer is better)
           - Acoustic: song.acousticness if user.likes_acoustic, else 1 - song.acousticness
        2. Total score = genre_score + mood_score + energy_score + acoustic_score
        3. Sort songs by total score descending
        4. Return top k songs
        """
        scored_songs = []
        for song in self.songs:
            genre_score = 1.0 if song.genre == user.favorite_genre else 0.0
            mood_score = 1.0 if song.mood == user.favorite_mood else 0.0
            energy_score = 1.0 - abs(song.energy - user.target_energy)
            acoustic_score = song.acousticness if user.likes_acoustic else (1.0 - song.acousticness)
            total_score = genre_score + mood_score + energy_score + acoustic_score
            scored_songs.append((song, total_score))
        
        # Sort by score descending
        scored_songs.sort(key=lambda x: x[1], reverse=True)
        
        # Return top k songs
        return [song for song, score in scored_songs[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """
        Explain why this song was recommended for the user.
        """
        reasons = []
        
        if song.genre == user.favorite_genre:
            reasons.append(f"it matches your favorite genre '{user.favorite_genre}'")
        
        if song.mood == user.favorite_mood:
            reasons.append(f"it matches your favorite mood '{user.favorite_mood}'")
        
        energy_diff = abs(song.energy - user.target_energy)
        if energy_diff < 0.2:
            reasons.append(f"its energy level ({song.energy:.2f}) is close to your target ({user.target_energy:.2f})")
        elif energy_diff < 0.5:
            reasons.append(f"its energy level ({song.energy:.2f}) is somewhat close to your target ({user.target_energy:.2f})")
        
        if user.likes_acoustic and song.acousticness > 0.5:
            reasons.append(f"it's acoustic ({song.acousticness:.2f} acousticness) and you like acoustic music")
        elif not user.likes_acoustic and song.acousticness < 0.5:
            reasons.append(f"it's not very acoustic ({song.acousticness:.2f}) and you prefer non-acoustic music")
        
        if reasons:
            return f"This song was recommended because {', and '.join(reasons)}."
        else:
            return "This song was recommended as a general match to your preferences."

def load_songs(csv_path: str) -> List[Dict[str, str]]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    import csv
    songs = []
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> float:
    """Return a score for a song based on genre, mood, and energy preferences."""
    genre_score = 0.5 * (1.0 if song['genre'] == user_prefs['genre'] else 0.0)
    mood_score = 1.0 if song['mood'] == user_prefs['mood'] else 0.0
    energy_score = 2.0 * (1.0 - abs(float(song['energy']) - user_prefs['energy']))
    return genre_score + mood_score + energy_score

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Return the top k songs sorted by preference score."""
    # Calculate scores for all songs using list comprehension
    scored_songs = [
        (song, score_song(user_prefs, song), "Score based on preferences")
        for song in songs
    ]
    
    # Sort by score in descending order and return top k
    return sorted(scored_songs, key=lambda x: x[1], reverse=True)[:k]
