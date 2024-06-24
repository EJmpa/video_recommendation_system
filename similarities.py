from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_video_similarities(videos_df):
    videos_df['metadata'] = videos_df.apply(
        lambda x: x['category'] + ' ' + ' '.join(x['tags']), axis=1
        )
    
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(videos_df['metadata'])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    
    return cosine_sim


