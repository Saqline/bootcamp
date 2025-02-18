vectorizer = TfidfVectorizer(max_features=5000)  # Convert text to numerical data
X_tfidf = vectorizer.fit_transform(["I love AI", "AI is amazing"]).toarray()


from gensim.models import Word2Vec

sentences = [["i", "love", "ai"], ["ai", "is", "amazing"]]
w2v_model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)
word_vector = w2v_model.wv['ai']  # Get vector for word 'ai'
