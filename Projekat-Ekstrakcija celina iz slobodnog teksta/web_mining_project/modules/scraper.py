import feedparser

def scrape_bbc_rss(limit=20):
    url = "http://feeds.bbci.co.uk/news/rss.xml"
    try:
        feed = feedparser.parse(url)
        articles = []
        for entry in feed.entries[:limit]:
            title = entry.get('title', '')
            summary = entry.get('summary', '')
            text = f"{title}. {summary}"
            articles.append(text)
        print(f"✓ Prikupljeno {len(articles)} članaka sa BBC News")
        return articles
    except Exception as e:
        print(f"✗ Greška pri scraping-u: {e}")
        print("  Koristim demo tekst...")
        return [
            "Apple announced the new iPhone 15 in September with improved camera features",
            "Microsoft launched a new Azure AI service for enterprise customers",
            "Tesla is working on improving batteries for electric cars to extend range",
            "Elon Musk stated that AI will play a key role in future society",
            "Google is investing heavily in quantum computing research",
            "The iPhone 15 features USB-C port replacing the Lightning connector",
            "Azure AI offers natural language processing capabilities",
            "Electric vehicles are becoming more affordable for consumers",
            "Quantum computers could revolutionize cryptography and drug discovery",
            "Tim Cook presented the new Apple Watch during the keynote",
            "Microsoft CEO Satya Nadella emphasized cloud computing growth",
            "Tesla opened new Gigafactory in Texas for production",
            "OpenAI released GPT-4 with enhanced reasoning capabilities",
            "Google DeepMind announced breakthrough in protein folding",
            "Apple's market cap reached historic highs in 2024"
        ]
