from sklearn.metrics.pairwise import cosine_similarity
from data_preprocessing import preprocess_data

class search:
    def __init__(self):
        self.data, self.vectorizer, self.song_vectors = preprocess_data()
    def calculate_similarity(self, query):
        query_vector = self.vectorizer.transform([query])
        similarities = cosine_similarity(query_vector, self.song_vectors).flatten()
        sorted_indices = similarities.argsort()[::-1]
        return self.data, similarities, sorted_indices