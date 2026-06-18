import pickle

from sklearn.neighbors import NearestNeighbors


class ImageSearcher:

    def __init__(self):

        with open("artifacts/embeddings.pkl", "rb") as f:
            self.embeddings = pickle.load(f)

        with open("artifacts/filenames.pkl", "rb") as f:
            self.filenames = pickle.load(f)

        self.nn = NearestNeighbors(
            n_neighbors=6,
            metric="cosine"
        )

        self.nn.fit(self.embeddings)

    def search(self, feature):

        distances, indices = self.nn.kneighbors(
            [feature]
        )

        results = []

        for dist, idx in zip(
            distances[0][1:],
            indices[0][1:]
        ):

            results.append(
                {
                    "path": self.filenames[idx],
                    "score": round(
                        (1 - dist) * 100,
                        2
                    )
                }
            )

        return results