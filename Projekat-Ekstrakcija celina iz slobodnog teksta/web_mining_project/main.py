from modules.scraper import scrape_bbc_rss
from modules.ner_bert import ner_pipeline, extract_entities
from modules.embeddings import create_embeddings
from modules.clustering import find_optimal_k, run_kmeans
from modules.validation import run_validation
from modules.tfidf_keywords import get_top_keywords
from modules.visualization.pca_plot import plot_pca_clusters
from modules.visualization.wordcloud_plot import plot_wordclouds
from modules.visualization.network_graph import plot_entity_graph

import matplotlib.pyplot as plt

# 1. Prikupljanje teksta
articles = scrape_bbc_rss(limit=20)
text = ". ".join(articles)

# 2. NER BERT
entities = ner_pipeline(text)
entity_dict, entity_scores = extract_entities(entities)

# 3. Priprema rečenica
sentences = [s.strip() for s in text.split(".") if len(s.strip()) > 20]

# 4. Sentence-BERT embeddings
embeddings = create_embeddings(sentences)

# 5. Klasterovanje
optimal_k, silhouette_scores, inertias = find_optimal_k(embeddings)
labels, clusters = run_kmeans(embeddings, sentences, optimal_k)

# 6. Validacija
is_union_valid, duplicate_count, missing_sentences, extra_sentences, overlaps_found = run_validation(sentences, clusters)

# 7. TF-IDF ključne reči
cluster_keywords = {}
for cluster_id, sents in clusters.items():
    keywords = get_top_keywords(sents, top_n=5)
    cluster_keywords[cluster_id] = keywords

# 8. Vizualizacije
plot_pca_clusters(embeddings, labels, optimal_k, clusters)
plot_wordclouds(clusters)
plot_entity_graph(entities, sentences)

print("\n✅ Projekat uspešno pokrenut!")
