# 🧠 Projekat: Ekstrakcija celina iz slobodnog teksta

## 📘 Opis projekta  
Ovaj projekat ima za cilj **automatsku ekstrakciju tematskih celina iz slobodnog teksta** korišćenjem kombinacije modernih **NLP (Natural Language Processing)** tehnika.  
Projekat koristi **BERT NER model**, **Sentence-BERT embeddings**, **K-Means klasterovanje**, **TF-IDF analizu ključnih reči**, i **vizualizacije** radi prikaza strukture teksta.

Zamišljen je kao praktičan primer **web mining** sistema koji može pomoći u analizi velikih količina teksta – poput novinskih članaka, blogova ili dokumenata.

---

## ⚙️ Funkcionalnosti  

✅ Automatsko prikupljanje tekstova sa BBC RSS izvora  
✅ Prepoznavanje imenovanih entiteta pomoću BERT NER modela  
✅ Kreiranje Sentence-BERT vektorskih reprezentacija rečenica  
✅ Automatsko klasterovanje teksta pomoću K-Means algoritma  
✅ Validacija i evaluacija klastera  
✅ Generisanje ključnih reči korišćenjem TF-IDF algoritma  
✅ Vizualizacija rezultata:
- PCA graf klastera  
- WordCloud svake teme  
- Graf povezanosti entiteta  

---

## 🧩 Struktura projekta  

```
web_mining_project/
│
├─ modules/                     # Funkcionalni delovi projekta
│   ├─ __init__.py
│   ├─ scraper.py               # Prikupljanje vesti sa BBC RSS feed-a
│   ├─ ner_bert.py              # BERT NER pipeline i ekstrakcija entiteta
│   ├─ embeddings.py            # Sentence-BERT embeddings
│   ├─ clustering.py            # K-Means klasterovanje i optimalan broj klastera
│   ├─ validation.py            # Validacija i evaluacija klastera
│   ├─ tfidf_keywords.py        # TF-IDF analiza ključnih reči
│   ├─ visualization/           # Podfolder za sve vizualizacije
│   │   ├─ __init__.py
│   │   ├─ pca_plot.py          # PCA dijagram klastera
│   │   ├─ wordcloud_plot.py    # WordCloud prikaz tema
│   │   └─ network_graph.py     # Graf povezanosti entiteta
│
├─ results/                     # Folder gde se automatski čuvaju slike i grafici
│
├─ main.py                      # Glavni fajl koji pokreće ceo projekat
├─ README.md                    # Opis projekta
└─ requirements.txt              # Lista potrebnih Python biblioteka

```

## 🛠️ Instalacija i pokretanje  

1. **Kloniraj repozitorijum:**
   ```bash
   git clone https://github.com/Boxon00/Ekstrakcija_celina_iz_slobodnog_teksta.git
   cd Ekstrakcija_celina_iz_slobodnog_teksta/web_mining_project
   ```

2. **(Opcionalno) Kreiraj virtuelno okruženje:**
   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux/Mac
   venv\Scripts\activate         # Windows
   ```

3. **Instaliraj zavisnosti:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Pokreni projekat:**
   ```bash
   python main.py
   ```

---

## 📊 Rezultati i vizualizacije  

Projekat generiše sledeće vizualizacije:

- 🧩 **pca_plot.png** – prikaz klastera pomoću PCA dimenzionalne redukcije  
- ☁️ **wordclouds.png** – WordCloud prikaz ključnih reči za svaku temu  
- 🔗 **entity_graph.png** – graf povezanosti entiteta detektovanih BERT modelom

Sve slike se automatski čuvaju u folderu `results/`.

---

## 🧠 Korišćene tehnologije  

- **Python 3.10+**  
- **Transformers (Hugging Face)** – BERT modeli  
- **SentenceTransformers** – Sentence-BERT embeddings  
- **Scikit-learn** – KMeans, PCA i evaluacija  
- **Matplotlib / Seaborn** – Vizualizacije  
- **WordCloud** – Generisanje oblaka reči  
- **Requests / Feedparser** – Prikupljanje tekstova sa interneta  

---

## 🧾 Napomena  

Projekat je izrađen kao edukativni primer **NLP analize teksta** i demonstracija procesa **ekstrakcije tematskih celina**.  
Može poslužiti kao osnov za dalji razvoj alata za analizu novinskih članaka, tekstova sa društvenih mreža ili dokumenata.

---

## 📚 Zaključak  

Ovaj projekat uspešno povezuje više faza obrade prirodnog jezika — od prikupljanja i obrade teksta, preko ekstrakcije entiteta i vektorizacije rečenica, do klasterovanja i vizuelne prezentacije rezultata.  
Kroz upotrebu modernih modela kao što su **BERT** i **Sentence-BERT**, omogućeno je automatsko prepoznavanje tematskih celina i ključnih informacija.  
Rešenje može biti osnova za razvoj inteligentnih sistema za **analizu teksta, sumarizaciju sadržaja** i **istraživačke projekte u oblasti NLP-a**.

---

## 👨‍💻 Autor  

**Bojan [Boxon00]**  
📂 GitHub: [https://github.com/Boxon00](https://github.com/Boxon00)
