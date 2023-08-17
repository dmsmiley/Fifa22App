import plotly.graph_objects as go
import pandas as pd
import streamlit as st

data_file = 'fifa22data.csv'
df = pd.read_csv(data_file, index_col='FullName')

#User Selection _____________________________
player_1 = st.selectbox('Type First Player:', options=list(df.index.values))
player_2 = st.selectbox('Type Second Player: ', options=list(df.index.values),
                        index=1)

#Player Display_________________________________________

photo_1 = df.loc[player_1]['PhotoUrl']
photo_2 = df.loc[player_2]['PhotoUrl']

col1_1, col1_2 = st.columns(2)

with col1_1:
    st.subheader(player_1)
    st.markdown('#### Age: {}'.format(df.loc[player_1]['Age']))
    st.image(photo_1, use_column_width=True)

with col1_2:
    st.subheader(player_2)
    st.markdown('#### Age: {}'.format(df.loc[player_2]['Age']))
    st.image(photo_2, use_column_width=True)

#Player Information_____________________________________

club_logo_1 = df.loc[player_1]['Club Logo']
flag_1 = df.loc[player_1]['Flag']

club_logo_2 = df.loc[player_2]['Club Logo']
flag_2 = df.loc[player_2]['Flag']


col2_1, col2_2, col2_3, col2_4 = st.columns(4)


with col2_1:
    st.markdown("##### Club:")
    st.markdown("###### {}".format(df.loc[player_1]['Club']))
    st.image(club_logo_1, use_column_width=True)

with col2_2:
    st.markdown("##### Nationality:")
    st.markdown("###### {}".format(df.loc[player_1]['Nationality']))
    st.image(flag_1, use_column_width=True)

with col2_3:
    st.markdown("##### Club:")
    st.markdown("###### {}".format(df.loc[player_2]['Club']))
    st.image(club_logo_2, use_column_width=True)

with col2_4:
    st.markdown("##### Nationality:")
    st.markdown("###### {}".format(df.loc[player_2]['Nationality']))
    st.image(flag_2, use_column_width=True)


#Main Stats_____________________________________________

new_df = df.loc[[player_1,player_2]][['PaceTotal','ShootingTotal', 'PassingTotal',
                                        'DribblingTotal', 'DefendingTotal','PhysicalityTotal']]

#Radar Chart

# Customize colors for each plot
color1 = 'rgba(0, 128, 128, 0.5)'  # Hot pink with some transparency
color2 = 'rgba(255, 127, 80, 0.5)'   # Brown with some transparency

categories = list(new_df.columns)

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
    r=new_df.iloc[0],
    theta=categories,
    fill='toself', 
    name=new_df.index[0],
    line=dict(color=color1)
    ))

fig.add_trace(go.Scatterpolar(
    r=new_df.iloc[1],
    theta=categories,
    fill='toself',  
    name=new_df.index[1],
    line=dict(color=color2)
    ))

fig.update_layout(
    title=f"{new_df.index[0]} vs {new_df.index[1]}",
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 100]
        )),
    showlegend=True
    )

st.plotly_chart(fig)


#Expander Stats______________________________________________
expander = st.expander(label='Click to Compare All Stats')

add_stats = ['Height', 'Weight', 'Overall', 'Potential', 'Growth', 'TotalStats',
                'BaseStats', 'ValueEUR', 'WageEUR', 'ReleaseClause', 'IntReputation','WeakFoot', 'SkillMoves',
                'PaceTotal', 'ShootingTotal', 'PassingTotal', 'DribblingTotal',
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

with expander:
    stats_df = df.loc[[player_1,player_2]][add_stats]

    player_1_stat_list = list(stats_df.iloc[0][1:])
    player_2_stat_list = list(stats_df.iloc[1][1:])
    stats = list(stats_df.columns[1:])

    display_df = pd.DataFrame(list(zip(player_1_stat_list,player_2_stat_list,stats)), columns = [player_1,player_2,"Stats"]).set_index("Stats").style.highlight_max(color='#FFF8DC', axis=1)

    st.dataframe(display_df)

#Sidebar
st.sidebar.write(' ')
st.sidebar.write(' ')
st.sidebar.markdown("### Need Help Finding a Player?")
country_club = st.sidebar.selectbox('What Country is Their Club In? ', list(df['Club Country'].unique()))
league = st.sidebar.selectbox('What League is Their Club in?', list(df['Club League'][df['Club Country'] == country_club].unique()))
club = st.sidebar.selectbox('What Club Do They Play For?', list(df['Club'][df['Club League'] == league].unique()))
player = st.sidebar.selectbox('Who is the Player?', list(df[df['Club'] == club].index.values))
st.sidebar.write(player)
