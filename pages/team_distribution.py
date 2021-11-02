import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np




def app():
    data_file = 'fifa22data.csv'
    df = pd.read_csv(data_file, index_col=["FullName"])

    potential_stats = ['Age', 'Height', 'Weight', 'Overall', 'Potential', 'Growth', 'TotalStats',
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

    league = st.selectbox('Type League: ', options=list(set([x for x in df['Club League'] if pd.isnull(x) == False])), index = 3)
    stat = st.selectbox('Stat: ', options=potential_stats)

    newer_df = df[df.isin([league]).any(axis=1)]

    fig = px.box(newer_df,
               y = stat,
               x = 'Club',
                 width = 800)


    st.plotly_chart(fig)

    expander = st.expander(label= f'Player {stat} by Club in {league}')

    with expander:
        clubs = st.selectbox("Club:", options=list(set([x for x in newer_df['Club'] if pd.isnull(x) == False])))

        expander_df = df[df.isin([clubs]).any(axis=1)].sort_values(by=[stat], ascending=False)[stat]

        st.dataframe(expander_df)