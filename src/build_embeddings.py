import os
import pickle

from tqdm import tqdm

from feature_extractor import FeatureExtractor


extractor = FeatureExtractor()

embeddings = []
filenames = []

folder = "dataset/images"

for file in tqdm(os.listdir(folder)):

    path = os.path.join(folder, file)

    try:

        feature = extractor.extract(path)

        embeddings.append(feature)

        filenames.append(path)

    except Exception as e:

        print(file, e)

with open("artifacts/embeddings.pkl", "wb") as f:
    pickle.dump(embeddings, f)

with open("artifacts/filenames.pkl", "wb") as f:
    pickle.dump(filenames, f)

print("Done")