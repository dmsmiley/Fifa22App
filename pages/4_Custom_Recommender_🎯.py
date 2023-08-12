import pandas as pd
import streamlit as st
from sklearn.neighbors import NearestNeighbors
from scipy.sparse import csr_matrix
from sklearn.preprocessing import StandardScaler
import numpy as np


data_file = 'fifa22data.csv'
df = pd.read_csv(data_file, index_col='FullName')

df_columns = ['Potential', 'Growth', 'TotalStats', 'BaseStats', 'IntReputation', 'WeakFoot', 'SkillMoves',
                'Acceleration', 'SprintSpeed', 'HeadingAccuracy', 'Interceptions', 'Marking', 'SlidingTackle',
                'StandingTackle', 'Aggression', 'Jumping', 'Stamina', 'Strength',
                'Finishing', 'LongShots', 'Penalties',
                'Positioning', 'ShotPower', 'Volleys', 'Crossing', 'Curve',
                'FKAccuracy', 'LongPassing', 'ShortPassing', 'Vision', 'Agility',
                'Balance', 'BallControl', 'Composure', 'Dribbling', 'Reactions']

knn_df = df[:1500][df_columns]

#Set Attributes
df_1, df_2, df_3, df_4 = np.array_split(df_columns, 4)

st.header('All Stats:')

col1, col2, col3, col4 = st.columns(4)

player_stats = []

with col1:
    i=0
    st.markdown('##### Overall:')
    for x in df_1:
        z = st.number_input(f'{x} ({knn_df[x].min()} to {knn_df[x].max()})', min_value=knn_df[x].min(), max_value=knn_df[x].max(),
                            value=int(knn_df[x].mean()))
        player_stats.append(z)
        if x == 'SkillMoves':
            st.markdown('##### Pace:')
        i+=1

with col2:
    i = 0
    st.markdown('##### Defending:')
    for x in df_2:
        z = st.number_input(f'{x} ({knn_df[x].min()} to {knn_df[x].max()})', min_value=knn_df[x].min(), max_value=knn_df[x].max(),
                            value=int(knn_df[x].mean()))
        if x == 'StandingTackle':
            st.markdown('##### Physical:')
        player_stats.append(z)
        i += 1


with col3:
    i = 0
    st.markdown('##### Shooting:')
    for x in df_3:
        z = st.number_input(f'{x} ({knn_df[x].min()} to {knn_df[x].max()})', min_value=knn_df[x].min(), max_value=knn_df[x].max(),
                            value=int(knn_df[x].mean()))
        if x == 'Volleys':
            st.markdown('##### Passing:')
        player_stats.append(z)
        i += 1

with col4:
    i = 0
    st.markdown('##### Passing (cont.):')
    for x in df_4:
        z = st.number_input(f'{x} ({knn_df[x].min()} to {knn_df[x].max()})', min_value=knn_df[x].min(), max_value=knn_df[x].max(),
                            value=int(knn_df[x].mean()))
        if x == 'Vision':
            st.markdown('##### Dribbling:')
        player_stats.append(z)
        i += 1

#player =
player_stats.insert(0, 'player')
col_names = ["FullName"] + df_columns

#top_recs = list(rec_df[rec_df['search_player'] == {}]['rec_player'])

# KNN
# add player to top of dataframe
df2 = pd.DataFrame(player_stats).transpose()
df2.columns = col_names
df2.set_index(["FullName"], inplace=True)
knn_df = pd.concat([df2, knn_df])


knn_scaled = StandardScaler().fit_transform(knn_df)
knn_final = pd.DataFrame(index=knn_df.index, columns=knn_df.columns, data=knn_scaled)

feature_matrix = csr_matrix(knn_final.values)
knn = NearestNeighbors(metric='cosine', algorithm='brute')
knn.fit(feature_matrix)

player_list = []
rec_list = []

for player in knn_final.index:
    distances, indices = knn.kneighbors(knn_final.loc[player, :].values.reshape(1, -1), n_neighbors=4)

    for elem in range(0, len(distances.flatten())):
        if elem == 0:
            player_list.append([player])
        else:
            rec_list.append([player, elem, knn_final.index[indices.flatten()[elem]], distances.flatten()[elem]])

rec_df = pd.DataFrame(rec_list, columns=['search_player', 'rec_number', 'rec_player', 'distance_score'])

# PLayer List
top_recs = list(rec_df[rec_df['search_player'] == 'player']['rec_player'])

#Add Rec Players

x = 0
i = 1

col1_1, col1_2 = st.columns(2)

with col1_1:
    st.image(df.loc[top_recs[x]]['PhotoUrl'])
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')

st.markdown('***')

with col1_2:
    st.markdown(f"#### {i}. {top_recs[x]}")
    st.markdown(f"##### Club: {df.loc[top_recs[x]]['Club']}")
    st.markdown(f"##### Overall: {df.loc[top_recs[x]]['Overall']}")
    st.markdown(f"##### Pace: {df.loc[top_recs[x]]['PaceTotal']}")
    st.markdown(f"##### Shooting: {df.loc[top_recs[x]]['ShootingTotal']}")
    st.markdown(f"##### Passing: {df.loc[top_recs[x]]['PassingTotal']}")
    st.markdown(f"##### Dribbling: {df.loc[top_recs[x]]['DribblingTotal']}")
    st.markdown(f"##### Defending: {df.loc[top_recs[x]]['DefendingTotal']}")
    st.markdown(f"##### Physicality: {df.loc[top_recs[x]]['PhysicalityTotal']}")
    st.write('')

x += 1
i += 1

col2_1, col2_2 = st.columns(2)

with col2_1:
    st.image(df.loc[top_recs[x]]['PhotoUrl'])
    st.write('')
    st.write('')
    st.write('')

st.markdown('***')

with col2_2:
    st.markdown(f"#### {i}. {top_recs[x]}")
    st.markdown(f"##### Club: {df.loc[top_recs[x]]['Club']}")
    st.markdown(f"##### Overall: {df.loc[top_recs[x]]['Overall']}")
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
    st.write('')
    st.write('')
    st.write('')

st.markdown('***')

with col3_2:
    st.markdown(f"#### {i}. {top_recs[x]}")
    st.markdown(f"##### Club: {df.loc[top_recs[x]]['Club']}")
    st.markdown(f"##### Overall: {df.loc[top_recs[x]]['Overall']}")
    st.markdown(f"##### Pace: {df.loc[top_recs[x]]['PaceTotal']}")
    st.markdown(f"##### Shooting: {df.loc[top_recs[x]]['ShootingTotal']}")
    st.markdown(f"##### Passing: {df.loc[top_recs[x]]['PassingTotal']}")
    st.markdown(f"##### Dribbling: {df.loc[top_recs[x]]['DribblingTotal']}")
    st.markdown(f"##### Defending: {df.loc[top_recs[x]]['DefendingTotal']}")
    st.markdown(f"##### Physicality: {df.loc[top_recs[x]]['PhysicalityTotal']}")
