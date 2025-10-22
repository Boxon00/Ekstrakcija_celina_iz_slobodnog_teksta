from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from collections import defaultdict
import numpy as np

def find_optimal_k(embeddings, k_min=2, k_max=8):
    silhouette_scores = []
    inertias = []
    K_range = range(k_min, min(k_max, len(embeddings)))

    for k in K_range:
        kmeans_temp = KMeans(n_clusters=k, random_state=42, n_init=10)
        labels_temp = kmeans_temp.fit_predict(embeddings)
        score = silhouette_score(embeddings, labels_temp)
        silhouette_scores.append(score)
        inertias.append(kmeans_temp.inertia_)
        print(f"K={k}: Silhouette={score:.4f}, Inertia={kmeans_temp.inertia_:.2f}")

    optimal_k = K_range[np.argmax(silhouette_scores)]
    print(f"✓ Optimalan broj klastera: {optimal_k}")
    return optimal_k, silhouette_scores, inertias

def run_kmeans(embeddings, sentences, n_clusters):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    labels = kmeans.fit_predict(embeddings)
    clusters = defaultdict(list)
    for sentence, label in zip(sentences, labels):
        clusters[label].append(sentence)
    return labels, clusters
