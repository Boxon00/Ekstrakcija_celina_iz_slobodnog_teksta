# Web Mining Project

Kratak opis: Projekat za ekstrakciju celina iz slobodnog teksta i analizu (scraping, NER, embeddings, klasterovanje, vizualizacija).

Struktura projekta:

- `main.py` - Glavni fajl za pokretanje projekta
- `requirements.txt` - Lista Python biblioteka
- `modules/` - Svi glavni moduli projekta
  - `scraper.py` - Prikupljanje teksta sa weba
  - `ner_bert.py` - BERT NER pipeline i ekstrakcija entiteta
  - `embeddings.py` - Sentence-BERT embeddings
  - `clustering.py` - KMeans klasterovanje i izbor optimalnog K
  - `validation.py` - Matematička validacija unije klastera
  - `tfidf_keywords.py` - TF-IDF analiza ključnih reči
  - `visualization/` - Vizualizacije
    - `pca_plot.py` - PCA vizualizacija klastera
    - `wordcloud_plot.py` - WordCloud vizualizacija
    - `network_graph.py` - Graf povezanosti entiteta
- `results/` - Output folder za slike i rezultate

Next steps:
- Popuniti module sa stubovima/funkcijama
- Dodati `requirements.txt` sa potrebnim paketima
- Inicijalizovati git i dodati `.gitignore`

Autor: (dodajte svoje ime)
