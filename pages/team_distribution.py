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

    col1_1, col1_2, col1_3 = st.columns((1,2,1))

    with col1_1:
        st.empty()

    with col1_2:
        league = st.selectbox('Type League: ', options=list(set([x for x in df['Club League'] if pd.isnull(x) == False])), index = 3)
        stat = st.selectbox('Stat:', options=potential_stats)

        newer_df = df[df.isin([league]).any(axis=1)]

    with col1_3:
        st.empty()

    fig = px.box(newer_df,
                 y=stat,
                 x='Club',
                 width=1600)

    st.plotly_chart(fig)

    col2_1, col2_2, col2_3 = st.columns(3)

    with col2_1:
        st.empty()

    with col2_2:
        expander1 = st.expander(label= f'Player {stat} by Club in {league}')

        with expander1:
            clubs = st.selectbox("Club:", options=list(set([x for x in newer_df['Club'] if pd.isnull(x) == False])))

            expander1_df = df[df.isin([clubs]).any(axis=1)].sort_values(by=[stat], ascending=False)[stat]
            logo_df = df[df.isin([clubs]).any(axis=1)]['Club Logo'][0]

            st.image(logo_df)
            st.dataframe(expander1_df)

    with col2_3:
        st.empty()


    col3_1, col3_2, col3_3 = st.columns((1,2,1))

    with col3_1:
        st.empty()

    with col3_2:
        expander2 = st.expander(label='Compare Clubs in Different Leagues')

        with expander2:
            clubs = st.multiselect("Club:", options=list(set([x for x in df['Club'] if pd.isnull(x) == False])))
            ex_stat = st.selectbox('Stat:  ', options=potential_stats)

            ex_club_df = df[df['Club'].isin(clubs)]

            fig = px.box(ex_club_df,
                         y = ex_stat,
                         x ='Club',
                         width = 750)

            st.plotly_chart(fig)

    with col3_3:
        st.empty()