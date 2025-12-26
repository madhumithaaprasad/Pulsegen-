from utils.embeddings import get_embedding, similarity
from utils.taxonomy import SEED_TOPICS

def deduplicate_topics(new_topics, existing_topics):
    deduped = {}

    # Precompute embeddings
    existing_embeddings = {
        topic: get_embedding([topic])[0]
        for topic in existing_topics
    }

    for topic in new_topics:
        topic_emb = get_embedding([topic])[0]
        matched = False

        for existing, emb in existing_embeddings.items():
            if similarity(topic_emb, emb) > 0.8:
                deduped.setdefault(existing, 0)
                deduped[existing] += 1
                matched = True
                break

        if not matched:
            deduped.setdefault(topic, 0)
            deduped[topic] += 1

    return deduped
