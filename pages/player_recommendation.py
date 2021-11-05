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
                  'CDMRating', 'RWBRating', 'LBRating', 'CBRating', 'RBRating', 'GKRating']

    knn_df = df[:1500][df_columns]

    # KNN
    knn_scaled = StandardScaler().fit_transform(knn_df)
    knn_final = pd.DataFrame(index=knn_df.index, columns=knn_df.columns, data=knn_scaled)

    feature_matrix = csr_matrix(knn_final.values)
    knn = NearestNeighbors(metric='cosine', algorithm='brute')
    knn.fit(feature_matrix)

    player_list = []
    rec_list = []

    for player in knn_final.index:
        distances, indices = knn.kneighbors(knn_final.loc[player, :].values.reshape(1, -1), n_neighbors=11)

        for elem in range(0, len(distances.flatten())):
            if elem == 0:
                player_list.append([player])
            else:
                rec_list.append([player, elem, knn_final.index[indices.flatten()[elem]], distances.flatten()[elem]])

    rec_df = pd.DataFrame(rec_list, columns=['search_player', 'rec_number', 'rec_player', 'distance_score'])

    # PLayer Selection
    player = st.selectbox('Type First Player: ', options=list(df.index.values))

    top_recs = list(rec_df[rec_df['search_player'] == player]['rec_player'])

    colm_1, colm_2 = st.columns(2)
    with colm_1:
        st.image(df.loc[player]['PhotoUrl'])

    with colm_2:
        st.markdown(f"#### {player}")
        st.markdown(f"##### Pace: {df.loc[player]['PaceTotal']}")
        st.markdown(f"##### Shooting: {df.loc[player]['ShootingTotal']}")
        st.markdown(f"##### Passing: {df.loc[player]['PassingTotal']}")
        st.markdown(f"##### Dribbling: {df.loc[player]['DribblingTotal']}")
        st.markdown(f"##### Defending: {df.loc[player]['DefendingTotal']}")
        st.markdown(f"##### Physicality: {df.loc[player]['PhysicalityTotal']}")

    st.markdown('***')

    st.subheader(f'10 Players Most Like {player}:')

    '''
    This would be the preferred method,
    but there are spacing issues which affect aesthetics
    
    col1_1, col1_2 = st.columns(2)
    with col1_1:
        for x in range(0, len(top_recs)):
            st.image(df.loc[top_recs[x]]['PhotoUrl'])
            st.markdown('***')

    with col1_2:
        i = 1
        j = 1
        for x in range(0, len(top_recs)):
            st.markdown(f"#### {i}. {top_recs[x]}")
            st.markdown(f"##### Pace: {df.loc[top_recs[x]]['PaceTotal']}")
            st.markdown(f"##### Shooting: {df.loc[top_recs[x]]['ShootingTotal']}")
            st.markdown(f"##### Passing: {df.loc[top_recs[x]]['PassingTotal']}")
            st.markdown(f"##### Dribbling: {df.loc[top_recs[x]]['DribblingTotal']}")
            st.markdown(f"##### Defending: {df.loc[top_recs[x]]['DefendingTotal']}")
            st.markdown(f"##### Physicality: {df.loc[top_recs[x]]['PhysicalityTotal']}")
            for _ in range(j):
                st.write('')
            i += 1
            j += 1'''

    x = 0
    i = 1

    col1_1, col1_2 = st.columns(2)

    with col1_1:
        st.image(df.loc[top_recs[x]]['PhotoUrl'])
        st.markdown('***')

    with col1_2:
        st.markdown(f"#### {i}. {top_recs[x]}")
        st.markdown(f"##### Pace: {df.loc[top_recs[x]]['PaceTotal']}")
        st.markdown(f"##### Shooting: {df.loc[top_recs[x]]['ShootingTotal']}")
        st.markdown(f"##### Passing: {df.loc[top_recs[x]]['PassingTotal']}")
        st.markdown(f"##### Dribbling: {df.loc[top_recs[x]]['DribblingTotal']}")
        st.markdown(f"##### Defending: {df.loc[top_recs[x]]['DefendingTotal']}")
        st.markdown(f"##### Physicality: {df.loc[top_recs[x]]['PhysicalityTotal']}")

    x += 1
    i += 1

    col2_1, col2_2 = st.columns(2)

    with col2_1:
        st.image(df.loc[top_recs[x]]['PhotoUrl'])
        st.markdown('***')

    with col2_2:
        st.markdown(f"#### {i}. {top_recs[x]}")
        st.markdown(f"##### Pace: {df.loc[top_recs[x]]['PaceTotal']}")
        st.markdown(f"##### Shooting: {df.loc[top_recs[x]]['ShootingTotal']}")
        st.markdown(f"##### Passing: {df.loc[top_recs[x]]['PassingTotal']}")
        st.markdown(f"##### Dribbling: {df.loc[top_recs[x]]['DribblingTotal']}")
        st.markdown(f"##### Defending: {df.loc[top_recs[x]]['DefendingTotal']}")
        st.markdown(f"##### Physicality: {df.loc[top_recs[x]]['PhysicalityTotal']}")

    x += 1
    i += 1

    col3_1, col3_2 = st.columns(2)

    with col3_1:
        st.image(df.loc[top_recs[x]]['PhotoUrl'])
        st.markdown('***')

    with col3_2:
        st.markdown(f"#### {i}. {top_recs[x]}")
        st.markdown(f"##### Pace: {df.loc[top_recs[x]]['PaceTotal']}")
        st.markdown(f"##### Shooting: {df.loc[top_recs[x]]['ShootingTotal']}")
        st.markdown(f"##### Passing: {df.loc[top_recs[x]]['PassingTotal']}")
        st.markdown(f"##### Dribbling: {df.loc[top_recs[x]]['DribblingTotal']}")
        st.markdown(f"##### Defending: {df.loc[top_recs[x]]['DefendingTotal']}")
        st.markdown(f"##### Physicality: {df.loc[top_recs[x]]['PhysicalityTotal']}")

    x += 1
    i += 1

    col4_1, col4_2 = st.columns(2)

    with col4_1:
        st.image(df.loc[top_recs[x]]['PhotoUrl'])
        st.markdown('***')

    with col4_2:
        st.markdown(f"#### {i}. {top_recs[x]}")
        st.markdown(f"##### Pace: {df.loc[top_recs[x]]['PaceTotal']}")
        st.markdown(f"##### Shooting: {df.loc[top_recs[x]]['ShootingTotal']}")
        st.markdown(f"##### Passing: {df.loc[top_recs[x]]['PassingTotal']}")
        st.markdown(f"##### Dribbling: {df.loc[top_recs[x]]['DribblingTotal']}")
        st.markdown(f"##### Defending: {df.loc[top_recs[x]]['DefendingTotal']}")
        st.markdown(f"##### Physicality: {df.loc[top_recs[x]]['PhysicalityTotal']}")

    x += 1
    i += 1

    col5_1, col5_2 = st.columns(2)

    with col5_1:
        st.image(df.loc[top_recs[x]]['PhotoUrl'])
        st.markdown('***')

    with col5_2:
        st.markdown(f"#### {i}. {top_recs[x]}")
        st.markdown(f"##### Pace: {df.loc[top_recs[x]]['PaceTotal']}")
        st.markdown(f"##### Shooting: {df.loc[top_recs[x]]['ShootingTotal']}")
        st.markdown(f"##### Passing: {df.loc[top_recs[x]]['PassingTotal']}")
        st.markdown(f"##### Dribbling: {df.loc[top_recs[x]]['DribblingTotal']}")
        st.markdown(f"##### Defending: {df.loc[top_recs[x]]['DefendingTotal']}")
        st.markdown(f"##### Physicality: {df.loc[top_recs[x]]['PhysicalityTotal']}")

    x += 1
    i += 1

    col6_1, col6_2 = st.columns(2)

    with col6_1:
        st.image(df.loc[top_recs[x]]['PhotoUrl'])
        st.markdown('***')

    with col6_2:
        st.markdown(f"#### {i}. {top_recs[x]}")
        st.markdown(f"##### Pace: {df.loc[top_recs[x]]['PaceTotal']}")
        st.markdown(f"##### Shooting: {df.loc[top_recs[x]]['ShootingTotal']}")
        st.markdown(f"##### Passing: {df.loc[top_recs[x]]['PassingTotal']}")
        st.markdown(f"##### Dribbling: {df.loc[top_recs[x]]['DribblingTotal']}")
        st.markdown(f"##### Defending: {df.loc[top_recs[x]]['DefendingTotal']}")
        st.markdown(f"##### Physicality: {df.loc[top_recs[x]]['PhysicalityTotal']}")

    x += 1
    i += 1

    col7_1, col7_2 = st.columns(2)

    with col7_1:
        st.image(df.loc[top_recs[x]]['PhotoUrl'])
        st.markdown('***')

    with col7_2:
        st.markdown(f"#### {i}. {top_recs[x]}")
        st.markdown(f"##### Pace: {df.loc[top_recs[x]]['PaceTotal']}")
        st.markdown(f"##### Shooting: {df.loc[top_recs[x]]['ShootingTotal']}")
        st.markdown(f"##### Passing: {df.loc[top_recs[x]]['PassingTotal']}")
        st.markdown(f"##### Dribbling: {df.loc[top_recs[x]]['DribblingTotal']}")
        st.markdown(f"##### Defending: {df.loc[top_recs[x]]['DefendingTotal']}")
        st.markdown(f"##### Physicality: {df.loc[top_recs[x]]['PhysicalityTotal']}")

    x += 1
    i += 1

    col8_1, col8_2 = st.columns(2)

    with col8_1:
        st.image(df.loc[top_recs[x]]['PhotoUrl'])
        st.markdown('***')

    with col8_2:
        st.markdown(f"#### {i}. {top_recs[x]}")
        st.markdown(f"##### Pace: {df.loc[top_recs[x]]['PaceTotal']}")
        st.markdown(f"##### Shooting: {df.loc[top_recs[x]]['ShootingTotal']}")
        st.markdown(f"##### Passing: {df.loc[top_recs[x]]['PassingTotal']}")
        st.markdown(f"##### Dribbling: {df.loc[top_recs[x]]['DribblingTotal']}")
        st.markdown(f"##### Defending: {df.loc[top_recs[x]]['DefendingTotal']}")
        st.markdown(f"##### Physicality: {df.loc[top_recs[x]]['PhysicalityTotal']}")

    x += 1
    i += 1

    col9_1, col9_2 = st.columns(2)

    with col9_1:
        st.image(df.loc[top_recs[x]]['PhotoUrl'])
        st.markdown('***')

    with col9_2:
        st.markdown(f"#### {i}. {top_recs[x]}")
        st.markdown(f"##### Pace: {df.loc[top_recs[x]]['PaceTotal']}")
        st.markdown(f"##### Shooting: {df.loc[top_recs[x]]['ShootingTotal']}")
        st.markdown(f"##### Passing: {df.loc[top_recs[x]]['PassingTotal']}")
        st.markdown(f"##### Dribbling: {df.loc[top_recs[x]]['DribblingTotal']}")
        st.markdown(f"##### Defending: {df.loc[top_recs[x]]['DefendingTotal']}")
        st.markdown(f"##### Physicality: {df.loc[top_recs[x]]['PhysicalityTotal']}")

    x += 1
    i += 1

    col10_1, col10_2 = st.columns(2)

    with col10_1:
        st.image(df.loc[top_recs[x]]['PhotoUrl'])
        st.markdown('***')

    with col10_2:
        st.markdown(f"#### {i}. {top_recs[x]}")
        st.markdown(f"##### Pace: {df.loc[top_recs[x]]['PaceTotal']}")
        st.markdown(f"##### Shooting: {df.loc[top_recs[x]]['ShootingTotal']}")
        st.markdown(f"##### Passing: {df.loc[top_recs[x]]['PassingTotal']}")
        st.markdown(f"##### Dribbling: {df.loc[top_recs[x]]['DribblingTotal']}")
        st.markdown(f"##### Defending: {df.loc[top_recs[x]]['DefendingTotal']}")
        st.markdown(f"##### Physicality: {df.loc[top_recs[x]]['PhysicalityTotal']}")

    x += 1
    i += 1