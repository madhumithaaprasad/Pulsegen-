import os

# 🔴 Force Transformers to NEVER load TensorFlow
os.environ["TRANSFORMERS_NO_TF"] = "1"
os.environ["USE_TF"] = "0"

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Lightweight, CPU-friendly model
model = SentenceTransformer("all-MiniLM-L6-v2", device="cpu")

def get_embedding(texts):
    return model.encode(texts, show_progress_bar=False)

def similarity(vec1, vec2):
    return cosine_similarity([vec1], [vec2])[0][0]
