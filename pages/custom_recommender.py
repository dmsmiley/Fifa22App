import pandas as pd
import streamlit as st
from sklearn.neighbors import NearestNeighbors
from scipy.sparse import csr_matrix
from sklearn.preprocessing import StandardScaler

"""
Using KNN to determine how alike players are
"""

def app():
    data_file = 'fifa22data.csv'
    df = pd.read_csv(data_file, index_col='FullName')

    df_columns = ['Age', 'Height', 'Weight', 'Overall', 'Potential', 'Growth', 'TotalStats',
                  'BaseStats', 'ValueEUR', 'WageEUR', 'ReleaseClause', 'IntReputation',
                  'WeakFoot', 'SkillMoves', 'PaceTotal', 'ShootingTotal', 'PassingTotal', 'DribblingTotal',
                  'DefendingTotal', 'PhysicalityTotal', 'Crossing', 'Finishing', 'HeadingAccuracy',
                  'ShortPassing', 'Volleys', 'Dribbling', 'Curve', 'FKAccuracy',
                  'LongPassing', 'BallControl', 'Acceleration', 'SprintSpeed', 'Agility',
                  'Reactions', 'Balance', 'ShotPower', 'Jumping', 'Stamina', 'Strength',
                  'LongShots', 'Aggression', 'Interceptions', 'Positioning', 'Vision',
                  'Penalties', 'Composure', 'Marking', 'StandingTackle', 'SlidingTackle',
                  'GKDiving', 'GKHandling', 'GKKicking', 'GKPositioning', 'GKReflexes',
                  'STRating', 'LWRating', 'LFRating', 'CFRating', 'RFRating', 'RWRating',
                  'CAMRating', 'LMRating', 'CMRating', 'RMRating', 'LWBRating',
                  'CDMRating', 'RWBRating', 'LBRating', 'CBRating', 'RBRating','GKRating']

    kmeans_df = df[:1500][columns]