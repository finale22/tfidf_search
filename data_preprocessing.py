from sklearn.feature_extraction.text import TfidfVectorizer
from data_loader import load_data

def preprocess_data():
    data = load_data()
    data['artist+song'] = data['artist'] + ' ' + data['song']
    preprocessed_data = data.drop(columns=['link'])

    vectorizer = TfidfVectorizer()
    song_vectors = vectorizer.fit_transform(preprocessed_data['artist+song'])
    return preprocessed_data, vectorizer, song_vectors

