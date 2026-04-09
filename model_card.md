# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**VibeMixer 1.0**

---

## 2. Intended Use

This recommender suggests songs based on a user profile. It uses genre, mood, and energy preferences. It is meant for classroom exploration and simple music demos. It is not a real streaming service.

---

## 3. How the Model Works

The model scores each song by checking if it matches the user's genre and mood. It also measures how close the song's energy is to the user's target energy. Songs with higher scores are ranked higher. The goal is to surface songs that feel right for a given mood and energy level.

---

## 4. Data

The dataset has 17 songs. It includes pop, lofi, rock, ambient, jazz, synthwave, indie pop, hip hop, electronic, folk, reggae, and other styles. The songs have mood labels like happy, chill, intense, relaxed, and calm. The dataset is small and does not cover every genre or every kind of listening situation.

---

## 5. Strengths

The system works well for clear preference profiles. It can find upbeat pop for high-energy happy listeners and calm lofi for chill listeners. It also picks intense rock when the profile asks for a hard, energetic sound. The model captures the idea that energy and mood matter a lot in music choice.

---

## 6. Limitations and Bias

The model often over-prioritizes energy and can create an "energy bubble." It may ignore songs that match genre or mood if their energy is too different from the profile. The dataset also has more pop and chill songs than niche styles. That makes some tastes less likely to be served well.

---

## 7. Evaluation

I tested three profiles: High-Energy Pop, Chill Lofi, and Deep Intense Rock. I checked the top 5 recommendations for each profile and compared how the outputs changed. I also tried changing the scoring weights and removing mood matching to see the effect. This helped verify that the model behaves as expected and that score changes affect ranking in a predictable way.

---

## 8. Future Work

1. Add more songs and more genres to reduce bias.
2. Include tempo, danceability, or acousticness as extra features.
3. Give users control over the importance of genre, mood, and energy.

---

## 9. Personal Reflection

The biggest learning moment was seeing how a few score changes can completely reshape the recommendation list. Using AI tools helped me generate ideas and check logic quickly, but I had to double-check the code and output because the suggestions were not always exact. It was surprising that such a simple scoring algorithm could still feel reasonable and reflect real listening preferences. Next, I would try adding more song features and letting the user adjust how much genre, mood, and energy matter.
