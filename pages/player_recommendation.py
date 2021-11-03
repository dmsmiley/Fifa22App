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
    kmeans_df = df[:1500][['PaceTotal','ShootingTotal', 'PassingTotal', 'DribblingTotal', 'DefendingTotal','PhysicalityTotal']]

    # KNN
    kmeans_scaled = StandardScaler().fit_transform(kmeans_df)
    kmeans_final = pd.DataFrame(index=kmeans_df.index, columns=kmeans_df.columns, data=kmeans_scaled)

    feature_matrix = csr_matrix(kmeans_final.values)
    knn = NearestNeighbors(metric='cosine', algorithm='brute')
    knn.fit(feature_matrix)

    player_list = []
    rec_list = []

    for player in kmeans_final.index:
        distances, indices = knn.kneighbors(kmeans_final.loc[player, :].values.reshape(1, -1), n_neighbors=7)

        for elem in range(0, len(distances.flatten())):
            if elem == 0:
                player_list.append([player])
            else:
                rec_list.append([player, elem, kmeans_final.index[indices.flatten()[elem]], distances.flatten()[elem]])

    rec_df = pd.DataFrame(rec_list, columns=['search_player', 'rec_number', 'rec_player', 'distance_score'])

    # PLayer Selection
    player = st.selectbox('Type First Player:', options=list(df.index.values))

    top_recs = list(rec_df[rec_df['search_player'] == player]['rec_player'])


    st.image(df.loc[player]['PhotoUrl'])
    st.subheader(f'Players Most Like {player}:')

    col1_1, col1_2 = st.columns(2)

    with col1_1:
        st.write(f'1. {top_recs[0]}')
        st.image(df.loc[top_recs[0]]['PhotoUrl'])

    with col1_2:
        st.write(f'2. {top_recs[1]}')
        st.image(df.loc[top_recs[1]]['PhotoUrl'])

    col2_1, col2_2 = st.columns(2)

    with col2_1:
        st.write(f'3. {top_recs[2]}')
        st.image(df.loc[top_recs[2]]['PhotoUrl'])

    with col2_2:
        st.write(f'4. {top_recs[3]}')
        st.image(df.loc[top_recs[3]]['PhotoUrl'])

    col3_1, col3_2 = st.columns(2)

    with col3_1:
        st.write(f'5. {top_recs[4]}')
        st.image(df.loc[top_recs[4]]['PhotoUrl'])

    with col3_2:
        st.write(f'6. {top_recs[5]}')
        st.image(df.loc[top_recs[5]]['PhotoUrl'])