import streamlit as st
import plotly.express as px
import pandas as pd

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
                 width = 1500)


    st.plotly_chart(fig)

    expander1 = st.expander(label= f'Player {stat} by Club in {league}')

    with expander1:
        clubs = st.selectbox("Club:", options=list(set([x for x in newer_df['Club'] if pd.isnull(x) == False])))

        col1_e, col2_e = st.columns((2,1))

        expander1_df = df[df.isin([clubs]).any(axis=1)].sort_values(by=[stat], ascending=False)[stat]
        logo_df = df[df.isin([clubs]).any(axis=1)]['Club Logo'][0]

        with col1_e:
            st.dataframe(expander1_df)

        with col2_e:
            st.image(logo_df)



    expander2 = st.expander(label='Compare Clubs in Different Leagues')

    with expander2:
        clubs = st.multiselect("Club:", options=list(set([x for x in df['Club'] if pd.isnull(x) == False])))
        ex_stat = st.selectbox('Stat:  ', options=potential_stats)

        ex_club_df = df[df['Club'].isin(clubs)]

        fig = px.box(ex_club_df,
                     y = ex_stat,
                     x ='Club',
                     width = 1400)

        st.plotly_chart(fig)
