# Visual Product Retrieval System using Deep Learning Embeddings

## Overview

Visual Product Retrieval System is a computer vision application that retrieves visually similar fashion products using deep learning image embeddings. The system extracts high-dimensional feature representations from product images using a pretrained ResNet50 model and performs similarity based retrieval to recommend relevant products from a fashion catalog.

The application provides an interactive interface where users can upload a fashion product image and receive visually similar recommendations in real time.

---

## Features

* Upload a fashion product image
* Deep feature extraction using ResNet50
* Visual similarity search using K-Nearest Neighbors (KNN)
* Cosine similarity-based retrieval
* Real-time recommendation generation
* Interactive Streamlit dashboard
* Fashion product metadata integration

---

## Tech Stack

* Python
* PyTorch
* ResNet50
* Scikit-Learn
* Streamlit
* Pandas
* NumPy
* Pillow

---

## System Architecture

Input Image
↓
ResNet50 Feature Extractor
↓
2048-D Feature Embeddings
↓
KNN + Cosine Similarity Search
↓
Top-K Similar Product Recommendations

---

## Dataset

The project utilizes product images and metadata derived from the Myntra Fashion Dataset.

Dataset Components:

* Product Images
* Product Metadata
* Category Information
* Product Attributes

---

## Project Workflow

1. Download product images from the dataset.
2. Generate feature embeddings using ResNet50.
3. Store embeddings for efficient retrieval.
4. Upload a query image.
5. Extract query image embeddings.
6. Perform similarity search.
7. Display top matching products.

---

## Results

* Generated embeddings for 2,000+ fashion product images.
* Achieved real-time image retrieval with low latency.
* Successfully retrieved visually similar products based on learned image representations.

---

## Future Enhancements

* Integrate FAISS for scalable vector search.
* Replace ResNet50 with CLIP embeddings.
* Add FastAPI backend services.
* Implement Precision@K and Recall@K evaluation metrics.
* Deploy application on cloud infrastructure.

---

## Author

**Devanshi Pandey**



Focused on Artificial Intelligence, Machine Learning, Computer Vision, and Generative AI.
