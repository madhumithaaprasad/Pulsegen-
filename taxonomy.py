# utils/taxonomy.py

import re

# Canonical topic labels used across the system
SEED_TOPICS = {
    "Customer Service - Negative": [
        "poor service", "bad service", "worst service", "bakvas service",
        "customer service", "very poor service", "bad customer support"
    ],
    "Delivery Issues": [
        "late delivery", "order cancel", "cancel after", "delivery issue",
        "not delivered", "delay"
    ],
    "Pricing & Charges": [
        "high charge", "shipping charge", "delivery charge",
        "very high price", "costly"
    ],
    "Discounts & Offers": [
        "no offers", "not giving discount", "less offers",
        "no discount"
    ],
    "Food Quality - Positive": [
        "nice food", "good food", "healthy food", "tasty",
        "food good"
    ],
    "Overall Experience - Positive": [
        "good", "super", "amazing", "fantastic",
        "best", "wow", "nice", "love"
    ],
    "Overall Experience - Negative": [
        "bad experience", "worst experience", "very bad",
        "not good", "poor experience"
    ]
}

def normalize_topic(review: str) -> str:
    """
    Maps a raw review string to a normalized business-friendly topic.
    """
    review = review.lower()

    for topic, keywords in SEED_TOPICS.items():
        for kw in keywords:
            if re.search(rf"\b{re.escape(kw)}\b", review):
                return topic

    return "Other"
