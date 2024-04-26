#This file is written so that the multiprocessing function can run correctly in Jupyter

import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

def cos_similarity_mp(user_df,trackid_a, segments):
    
    def cosine_similarity_opt3(user_df, trackid_a, track_b):
        columns = ['danceability', 'energy', 'acousticness', 'instrumentalness', 'liveness', 'valence']
        track_a = user_df.loc[trackid_a][columns]
        track_b = track_b[columns]
        vector_a = np.array(track_a)
        vector_b = np.array(track_b)

        dot_product = np.dot(vector_a, vector_b)

        magnitude_a = np.linalg.norm(vector_a)
        magnitude_b = np.linalg.norm(vector_b)

        return dot_product / (magnitude_a * magnitude_b)
    

    scores = segments.apply(lambda x: cosine_similarity_opt3(user_df, trackid_a, x), axis=1)
    
    return scores
