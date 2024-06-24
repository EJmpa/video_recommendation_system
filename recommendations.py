from load_data import load_data
from similarities import calculate_video_similarities


def get_recommendations(user_id, n):

  users_df, videos_df = load_data('data/data.json')
  cosine_sim = calculate_video_similarities(videos_df)

  user_watch_history = users_df[users_df['user_id'] == user_id]['watch_history'].values[0]

  watched_indices = [
      videos_df[videos_df['video_id'] == vid].index[0]
      for vid in user_watch_history
      ]

  sim_scores = cosine_sim[watched_indices].mean(axis=0)
  sim_scores_indices = sim_scores.argsort()[::-1]

  recommended_video_ids = [
      videos_df.iloc[i]['video_id']
      for i in sim_scores_indices
      if i not in watched_indices][:n]
  
  return recommended_video_ids
