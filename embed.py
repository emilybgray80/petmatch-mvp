import numpy as np

def generate_embedding(image_path: str):
    # Placeholder: returns a random vector to simulate an embedding
    np.random.seed(abs(hash(image_path)) % (10 ** 6))
    embedding = np.random.rand(10).tolist()
    return embedding
