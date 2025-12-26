# agents/topic_agent.py

from sklearn.cluster import DBSCAN
from utils.embeddings import get_embedding
from utils.taxonomy import normalize_topic

def extract_topics(reviews):
    # Step 1: Get embeddings for all reviews
    embeddings = get_embedding(reviews)

    # Step 2: Cluster similar reviews
    clustering = DBSCAN(
        eps=0.35,       # cosine distance threshold
        min_samples=3,  # min reviews per cluster
        metric="cosine"
    ).fit(embeddings)

    cluster_topics = {}
    for review, label in zip(reviews, clustering.labels_):
        if label == -1:  # ignore outliers
            continue
        cluster_topics.setdefault(label, []).append(review)

    # Step 3: For each cluster, pick representative review and normalize topic
    topics = []
    for cluster_reviews in cluster_topics.values():
        rep_review = cluster_reviews[0]   # first review as representative
        topic = normalize_topic(rep_review)
        topics.append(topic)

    return topics


