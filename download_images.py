import os
import pandas as pd
import requests
from tqdm import tqdm

# Load CSV
df = pd.read_csv("images.csv")

# Number of images to download
df = df.head(2000)

os.makedirs("dataset/images", exist_ok=True)

for _, row in tqdm(df.iterrows(), total=len(df)):

    filename = row["filename"]
    url = row["link"]

    save_path = os.path.join(
        "dataset/images",
        filename
    )

    if os.path.exists(save_path):
        continue

    try:

        response = requests.get(
            url,
            timeout=10
        )

        if response.status_code == 200:

            with open(save_path, "wb") as f:
                f.write(response.content)

    except Exception as e:

        print(
            f"Failed {filename}: {e}"
        )

print("Download Complete")