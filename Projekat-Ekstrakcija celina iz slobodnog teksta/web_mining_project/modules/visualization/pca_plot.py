import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import numpy as np

def plot_pca_clusters(embeddings, labels, optimal_k, clusters):
    pca = PCA(n_components=2, random_state=42)
    embeddings_2d = pca.fit_transform(embeddings)
    
    plt.figure(figsize=(12, 8))
    colors = plt.cm.Set3(np.linspace(0, 1, optimal_k))
    
    for i in range(optimal_k):
        mask = labels == i
        plt.scatter(
            embeddings_2d[mask, 0],
            embeddings_2d[mask, 1],
            c=[colors[i]],
            label=f'Celina {i+1} ({sum(mask)} rek.)',
            s=100,
            alpha=0.7,
            edgecolors='black',
            linewidth=0.5
        )
    
    centers = []
    for i in range(optimal_k):
        mask = labels == i
        centers.append(embeddings[mask].mean(axis=0))
    centers_2d = pca.transform(np.array(centers))
    
    plt.scatter(
        centers_2d[:, 0], 
        centers_2d[:, 1], 
        c='red', 
        marker='X', 
        s=300, 
        edgecolors='black', 
        linewidth=2, 
        label='Centri'
    )
    
    plt.xlabel('PCA Komponenta 1')
    plt.ylabel('PCA Komponenta 2')
    plt.title('PCA vizualizacija klastera')
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig("results/pca_plot.png")
    plt.show()