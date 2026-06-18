# AI-Powered Visual Product Search Engine

## Overview

This project is an image-based product retrieval system that recommends visually similar fashion products using deep learning image embeddings.

The system leverages a pretrained ResNet50 model to extract feature representations from product images and uses K-Nearest Neighbors (KNN) with cosine similarity to retrieve the most visually similar products from a fashion catalog.

## Features

* Upload a fashion product image
* Retrieve top-5 visually similar products
* Deep learning feature extraction using ResNet50
* Similarity search using KNN
* Product metadata display
* Interactive Streamlit web interface

## Tech Stack

* Python
* PyTorch
* ResNet50
* Scikit-Learn
* Streamlit
* Pandas

## Dataset

Myntra Fashion Product Dataset

## Architecture

Image → ResNet50 → 2048-D Embedding → KNN Search → Similar Products

## Results

The system generates image embeddings for fashion products and retrieves visually similar items in real time, achieving sub-second search latency on the indexed catalog.

## Future Improvements

* EfficientNet-based embeddings
* FAISS similarity search
* Category-aware retrieval
* Larger product catalog
* Multi-modal search using image and text
