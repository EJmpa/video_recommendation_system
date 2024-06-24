import pandas as pd
import json


def load_data(json_path):
    with open(json_path, 'r') as file:
        data = json.load(file)
    users_df = pd.DataFrame(data['users'])
    videos_df = pd.DataFrame(data['videos'])
    
    return users_df, videos_df
