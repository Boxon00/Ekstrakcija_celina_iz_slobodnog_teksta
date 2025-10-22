import matplotlib.pyplot as plt
from wordcloud import WordCloud

def plot_wordclouds(clusters):
    optimal_k = len(clusters)
    fig, axes = plt.subplots(1, optimal_k, figsize=(6*optimal_k, 5))
    if optimal_k == 1:
        axes = [axes]
    for cluster_id, ax in enumerate(axes):
        cluster_text = " ".join(clusters[cluster_id])
        try:
            wordcloud = WordCloud(
                width=800,
                height=400,
                background_color='white',
                colormap='viridis',
                max_words=50,
                stopwords={'the', 'a', 'an', 'in', 'on', 'at', 'to', 'for'}
            ).generate(cluster_text)
            ax.imshow(wordcloud, interpolation='bilinear')
            ax.set_title(f'Celina {cluster_id + 1}')
            ax.axis('off')
        except:
            ax.text(0.5, 0.5, 'Nedovoljno teksta', ha='center', va='center')
            ax.axis('off')
    plt.tight_layout()
    plt.savefig("results/wordclouds.png")
    plt.show()
