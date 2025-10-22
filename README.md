# 🧠 Ekstrakcija celina iz slobodnog teksta

Ovaj projekat predstavlja **kompletnu implementaciju NLP (Natural Language Processing)** sistema koji automatski analizira slobodan tekst, pronalazi **entitete (osobe, organizacije, lokacije, pojmove)**, zatim pomoću **Sentence-BERT** modela izračunava semantičke sličnosti između rečenica i grupiše ih u **tematske celine** (klastere).

Na kraju, rezultati se **vizualizuju** kroz više grafičkih prikaza: PCA dijagram, WordCloud prikaz i graf povezanosti entiteta.

Projekat je razvijen u **Python-u**, u okruženju **Visual Studio Code** (ili Google Colab) i koristi napredne alate iz oblasti mašinskog učenja, obrade prirodnog jezika i vizualizacije podataka.

---

## 🎯 Cilj projekta

Cilj ovog projekta je da prikaže kako se iz sirovog slobodnog teksta mogu **automatski izdvojiti tematske celine** pomoću kombinacije:
- BERT modela za ekstrakciju entiteta (NER),
- Sentence-BERT embeddings za semantičko razumevanje rečenica,
- KMeans algoritma za klasterovanje,
- TF-IDF analize za izdvajanje ključnih reči,
- i vizualizacija koje olakšavaju interpretaciju rezultata.

Ovakav sistem može biti osnova za:
- automatsku sumarizaciju vesti,  
- tematsko grupisanje dokumenata,  
- prepoznavanje trendova u tekstualnim podacima,  
- analizu sadržaja iz društvenih mreža ili RSS feedova.

---

## 🧩 Korišćene tehnologije i biblioteke

| Kategorija | Biblioteke / Alati | Opis |
|-------------|--------------------|-------|
| **NLP modeli** | `transformers`, `torch`, `sentence-transformers` | BERT modeli za NER i Sentence Embeddings |
| **Obrada podataka** | `scikit-learn`, `numpy`, `pandas` | Analiza, klasterovanje i evaluacija |
| **Web scraping** | `feedparser`, `requests`, `beautifulsoup4` | Prikupljanje tekstova sa BBC RSS feed-a |
| **Vizualizacija** | `matplotlib`, `seaborn`, `wordcloud`, `networkx` | Kreiranje grafičkih prikaza rezultata |
| **Razvojno okruženje** | `Visual Studio Code`, `Google Colab` | Mogućnost pokretanja lokalno i online |

---

## 📁 Struktura projekta

web_mining_project/
│
├─ modules/ # Glavni direktorijum sa funkcionalnim modulima
│ ├─ init.py
│ ├─ scraper.py # Prikupljanje tekstova sa BBC News RSS feeda
│ ├─ ner_bert.py # Named Entity Recognition (BERT)
│ ├─ embeddings.py # Kreiranje Sentence-BERT embeddings
│ ├─ clustering.py # Klasterovanje pomoću KMeans i izbor optimalnog K
│ ├─ validation.py # Validacija rezultata (poklapanje klastera)
│ ├─ tfidf_keywords.py # Analiza ključnih reči pomoću TF-IDF metode
│ │
│ └─ visualization/ # Vizualni prikazi rezultata
│ ├─ init.py
│ ├─ pca_plot.py # PCA prikaz klastera (2D redukcija)
│ ├─ wordcloud_plot.py # WordCloud prikaz po klasterima
│ └─ network_graph.py # Graf povezanosti entiteta
├─ results/ # Folder gde se automatski čuvaju slike (grafici)
├─ main.py # Glavni fajl koji pokreće sve module
├─ README.md
└─ requirements.txt # Lista svih potrebnih biblioteka

---

## ⚙️ Instalacija i pokretanje

### 1️⃣ Kloniranje repozitorijuma
```bash
git clone https://github.com/Boxon00/Ekstrakcija_celina_iz_slobodnog_teksta.git
cd Ekstrakcija_celina_iz_slobodnog_teksta/web_mining_project
2️⃣ Instalacija potrebnih biblioteka
pip install -r requirements.txt
3️⃣ Pokretanje projekta
python main.py

🔄 Tok obrade podataka
🔹 1. Prikupljanje tekstova (scraper.py)

Sistem koristi BBC RSS feed i automatski preuzima najnovije vesti.
Ukoliko nema internet konekcije, koristi se demo skup rečenica sa tehnološkim vestima.

🔹 2. Prepoznavanje entiteta (ner_bert.py)

Koristi se BERT model (dbmdz/bert-large-cased-finetuned-conll03-english) za NER (Named Entity Recognition).
Model detektuje entitete tipa:

PER (osobe),

ORG (organizacije),

LOC (lokacije),

MISC (ostali pojmovi).

🔹 3. Kreiranje embeddings (embeddings.py)

Za svaku rečenicu se računa Sentence-BERT embedding pomoću modela 'all-MiniLM-L6-v2'.
Ovi vektori predstavljaju semantičko značenje rečenica i koriste se za klasterovanje.

🔹 4. Klasterovanje (clustering.py)

Korišćenjem KMeans algoritma, rečenice se grupišu u tematske celine.
Funkcija find_optimal_k() pronalazi najbolji broj klastera pomoću silhouette score metrika.

🔹 5. Validacija (validation.py)

Proverava se da li su sve rečenice tačno raspoređene po klasterima bez duplikata ili preklapanja.

🔹 6. TF-IDF analiza (tfidf_keywords.py)

Za svaku celinu se izdvajaju ključne reči na osnovu važnosti (TF-IDF).

🔹 7. Vizualizacije (visualization/)

Sistem generiše tri vizualna prikaza:

PCA dijagram klastera (pca_plot.py)

WordCloud prikaz po klasterima (wordcloud_plot.py)

Graf povezanosti entiteta (network_graph.py)

Sve slike se automatski čuvaju u results/ folderu:

pca_plot.png

wordclouds.png

entity_graph.png

## 🧠 Arhitektura projekta

Tekst (RSS Feed)
     │
     ▼
[ BERT NER ] → Ekstrakcija entiteta
     │
     ▼
[ Sentence-BERT ] → Embeddings rečenica
     │
     ▼
[ KMeans klasterovanje ]
     │
     ├── TF-IDF analiza (ključne reči)
     ├── Validacija (duplikati, preklapanja)
     └── Vizualizacije (PCA, WordCloud, NetworkX)

## 📘 Potencijalne primene

Automatizovana klasifikacija vesti po temama

Sumarizacija dokumenata i tekstova

Prepoznavanje odnosa između entiteta

Tematska analiza postova, članaka i foruma

Generisanje znanja iz nestrukturisanih izvora podataka

## 🏁 Zaključak

Projekat "Ekstrakcija celina iz slobodnog teksta" prikazuje napredan pristup obradi prirodnog jezika i semantičkom grupisanju rečenica.
Kombinuje više tehnika — od web scrapinga i mašinskog učenja do vizualizacije i validacije rezultata.

Struktura projekta, modularnost i čitljivost koda omogućavaju lako proširenje sistema — npr. za srpski jezik, dodatne izvore teksta ili druge NLP zadatke.
