from sklearn.feature_extraction.text import TfidfVectorizer

def get_top_keywords(cluster_sentences, top_n=5):
    text_combined = " ".join(cluster_sentences)
    vectorizer = TfidfVectorizer(max_features=100, stop_words='english')
    try:
        tfidf_matrix = vectorizer.fit_transform([text_combined])
        feature_names = vectorizer.get_feature_names_out()
        scores = tfidf_matrix.toarray()[0]
        top_indices = scores.argsort()[-top_n:][::-1]
        keywords = [feature_names[i] for i in top_indices if scores[i] > 0]
        return keywords
    except:
        return []
