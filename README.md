# Video Recommendation System

This project implements a basic video recommendation system for a video streaming platform. The system suggests videos to users based on their watch history and video metadata.

## Table of Contents
- [Overview](#overview)
- [Data](#data)
- [Approach](#approach)
- [Requirements](#requirements)
- [Usage](#usage)
- [Docker](#docker)
- [Example](#example)
- [License](#license)

## Overview

The objective of this project is to provide a video recommendation system that leverages both collaborative filtering and content-based filtering techniques. The recommendations are generated based on the user's watch history and the similarity between video metadata.

## Data

The provided JSON data contains two main objects:

- `users`: An array of user objects, each containing:
  - `user_id`: Unique identifier for the user.
  - `name`: Name of the user.
  - `watch_history`: An array of video IDs the user has watched.

- `videos`: An array of video objects, each containing:
  - `video_id`: Unique identifier for the video.
  - `title`: Title of the video.
  - `category`: Category of the video.
  - `tags`: An array of relevant tags.
  - `duration`: Duration of the video.

## Approach

1. **Data Parsing**: Load the JSON data into pandas DataFrames for easy manipulation.
2. **Similarity Calculation**: Create a combined metadata string for each video and use TF-IDF to vectorize this metadata. Calculate cosine similarity between these vectors to measure video similarity.
3. **Recommendation Algorithm**:
   - Fetch the user's watch history.
   - Compute the mean similarity scores of all videos compared to the ones the user has watched.
   - Ensure that only unwatched videos are considered for recommendations.
   - Select the top N highest similarity scored videos that the user has not watched.

## Requirements

- \>= Python 3.9
- pandas
- scikit-learn
- Docker
- Docker Compose

Install the required Python packages using:
```sh
pip install -r requirements.txt

1. Clone the repository:

    ```sh
    git clone https://github.com/ejmpa/videorecommendationsystem.git
    cd videorecommendationsystem
    ```

2. Ensure you have Docker and Docker Compose installed on your machine.

## Usage
```sh
python main.py <user_id> <n>
```

Where <user_id> is the ID of the user and <n> is the number of recommendations to return.

Example:

python main.py 1 5

## Docker

**docker-compose up --build**

