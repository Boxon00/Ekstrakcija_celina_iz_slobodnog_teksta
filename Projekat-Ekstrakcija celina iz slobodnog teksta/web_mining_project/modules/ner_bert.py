from transformers import pipeline
from collections import defaultdict

ner_pipeline = pipeline(
    "ner",
    model="dbmdz/bert-large-cased-finetuned-conll03-english",
    aggregation_strategy="simple"
)

def extract_entities(entities):
    valid_types = ['PER', 'ORG', 'LOC', 'MISC']
    entity_dict = defaultdict(list)
    entity_scores = {}
    for e in entities:
        if e['entity_group'] in valid_types:
            word = e['word'].replace("##", "").strip()
            entity_dict[e['entity_group']].append(word)
            entity_scores[word] = e['score']
    return entity_dict, entity_scores
