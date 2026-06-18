import pandas as pd

import os
class MetadataManager:

    def __init__(self):

        self.df = pd.read_csv(
            "styles.csv",
            on_bad_lines="skip"
        )

        self.df["id"] = self.df["id"].astype(str)

    def get_product_info(self, image_path):

       

        image_id = os.path.basename(image_path)
        image_id = image_id.replace(".jpg", "")

        print("Image Path:", image_path)
        print("Extracted ID:", image_id)

        row = self.df[self.df["id"] == image_id]

        print("Matches Found:", len(row))

        if row.empty:
            return None

        row = row.iloc[0]

        return {
            "name": row["productDisplayName"],
            "gender": row["gender"],
            "category": row["masterCategory"],
            "subcategory": row["subCategory"],
            "article_type": row["articleType"],
            "color": row["baseColour"],
            "usage": row["usage"],
            "season": row["season"]
        }
