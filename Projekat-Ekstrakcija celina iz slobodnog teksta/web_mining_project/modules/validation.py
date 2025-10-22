def run_validation(sentences, clusters):
    """Matematička validacija unije klastera"""
    all_clustered_sentences = []
    for cluster_id, sents in clusters.items():
        all_clustered_sentences.extend(sents)

    original_set = set(sentences)
    clustered_set = set(all_clustered_sentences)

    is_union_valid = (original_set == clustered_set)
    missing_sentences = original_set - clustered_set
    duplicate_count = len(all_clustered_sentences) - len(clustered_set)
    extra_sentences = clustered_set - original_set

    cluster_sets = {cid: set(sents) for cid, sents in clusters.items()}
    overlaps_found = False
    overlap_details = []
    for i in range(len(cluster_sets)):
        for j in range(i+1, len(cluster_sets)):
            overlap = cluster_sets[i] & cluster_sets[j]
            if overlap:
                overlaps_found = True
                overlap_details.append((i+1, j+1, len(overlap)))

    return is_union_valid, duplicate_count, missing_sentences, extra_sentences, overlaps_found
