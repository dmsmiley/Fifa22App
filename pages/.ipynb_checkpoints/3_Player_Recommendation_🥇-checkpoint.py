import pandas as pd
import streamlit as st
from sklearn.neighbors import NearestNeighbors
from scipy.sparse import csr_matrix
from sklearn.preprocessing import StandardScaler

# Load the dataset from a CSV file and perform initial preprocessing
# This includes removing any rows with missing 'ValueEUR' values,
# dropping duplicate entries based on the 'FullName' column,
# and setting 'FullName' as the index for easier data retrieval.
data_file = 'fifa22data.csv'
df = pd.read_csv(data_file)
df = df.dropna(subset=["ValueEUR"]).drop_duplicates(subset=["FullName"]).set_index('FullName')
# Convert the 'ValueEUR' column to thousands of Euros for st.slider range limit and set as integer for consistency.
df["ValueEUR"] = (df["ValueEUR"]/1000).astype(int)

# Display the title of the Streamlit app interface.
st.markdown("### Player Recommendation")

# Allow the user to select a player from a dropdown menu.
# The options are limited to the first 500 entries because of Streamlit limit.
player = st.selectbox('Type Target Player: ', options=list(df[:500].index.values))

# Implement a slider for users to select the maximum player value.
# This filters the players displayed based on their 'ValueEUR' attribute.
max_value = st.slider(
    "Select the Maximum Player Value:",
    min_value=int(df['ValueEUR'].min()),
    max_value=int(df['ValueEUR'].max()),
    value=int(df['ValueEUR'].max())
)

# Filter the main DataFrame to include only players below the selected maximum value.
df_filtered = df[df['ValueEUR'] <= max_value]

# Ensure that the player selected by the user is included in the filtered DataFrame,
# even if their value exceeds the selected maximum, to allow for comparison.
if player not in df_filtered.index:
    df_filtered = pd.concat([df.loc[[player]], df_filtered])

# Specify the columns from the DataFrame that are used for the KNN model.
# These columns represent player attributes considered in the recommendation algorithm.
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

# Prepare data for KNN model
knn_df = df_filtered[:1500][df_columns]

# Normalize the feature data using StandardScaler to have a mean of 0 and a variance of 1.
# This standardization improves the performance and accuracy of the KNN model.
scaler = StandardScaler()
knn_scaled = scaler.fit_transform(knn_df)

# Convert the normalized data back into a DataFrame to retain the original structure.
# This step allows for easier manipulation and access to the data moving forward.
knn_final = pd.DataFrame(data=knn_scaled, index=knn_df.index, columns=knn_df.columns)

# Convert the DataFrame to a compressed sparse row matrix to optimize memory usage.
# Sparse matrices are particularly useful when dealing with a large number of features.
feature_matrix = csr_matrix(knn_final.values)

# Initialize and fit the NearestNeighbors model using the cosine similarity metric.
# The 'brute' algorithm is specified for simplicity, but other algorithms could be considered for optimization.
knn_model = NearestNeighbors(metric='cosine', algorithm='brute')
knn_model.fit(feature_matrix)

# Initialize lists to store the results of the player recommendation algorithm.
player_list = []
rec_list = []

# Iterate through each player in the filtered DataFrame to find and store their nearest neighbors.
for _ in knn_final.index:
    player_data = knn_final.loc[_, :].values.reshape(1, -1)
    
    # Skip any players whose data does not match the expected shape (1, 71), indicating a potential issue with the data.
    if player_data.shape[1] != 71:
        print(f"Skipping {_} due to unexpected shape: {player_data.shape}")
        continue
    # Use the KNN model to find the 11 nearest neighbors for each player, based on the cosine similarity of their attributes.
    distances, indices = knn_model.kneighbors(knn_final.loc[_, :].values.reshape(1, -1), n_neighbors=11)

    # Store the results in lists, separating the first entry (the player themselves) from their recommendations.
    for elem in range(0, len(distances.flatten())):
        if elem == 0:
            # For the first element, which is the player itself, append to player_list
            player_list.append([player])
        else:
            # For other elements, which are the recommended neighbors, append to rec_list
            rec_list.append([_, elem, knn_final.index[indices.flatten()[elem]], distances.flatten()[elem]])
            
# Convert the list of recommendations into a DataFrame for easier display and manipulation in the Streamlit app.            
rec_df = pd.DataFrame(rec_list, columns=['search_player', 'rec_number', 'rec_player', 'distance_score'])

# Extract the top recommendations for the user-selected player to be displayed in the app.
top_recs = list(rec_df[rec_df['search_player'] == player]['rec_player'])

colm_1, colm_2 = st.columns(2)

# # Display the selected player's information and their recommendations
with colm_1:
    st.image(df.loc[player]['PhotoUrl'])
    st.write('')
    st.write('')

with colm_2:
    st.markdown(f"#### {player}")
    st.markdown(f"##### Value: {df.loc[player]['ValueEUR']}")
    st.markdown(f"##### Club: {df.loc[player]['Club']}")
    st.markdown(f"##### Overall: {df.loc[player]['Overall']}")
    st.markdown(f"##### Pace: {df.loc[player]['PaceTotal']}")
    st.markdown(f"##### Shooting: {df.loc[player]['ShootingTotal']}")
    st.markdown(f"##### Passing: {df.loc[player]['PassingTotal']}")
    st.markdown(f"##### Dribbling: {df.loc[player]['DribblingTotal']}")
    st.markdown(f"##### Defending: {df.loc[player]['DefendingTotal']}")
    st.markdown(f"##### Physicality: {df.loc[player]['PhysicalityTotal']}")

st.markdown('***')

# Display a subheader in the app to introduce the section where the top 10 player recommendations will be shown.
st.subheader(f'10 Players Most Like {player}:')

# Loop through the list of recommended players. The enumerate function is used to get both the index (starting from 1) and the player name.
for i, rec_player in enumerate(top_recs, start=1):
    # Create two columns in the Streamlit interface using the columns method. This layout will display each player's photo on the left and their information on the right.
    col_left, col_right = st.columns(2)

    # In the left column, display the player's photo using the image method. The photo URL is retrieved from the DataFrame based on the player's name.
    with col_left:
        st.image(df.loc[rec_player]['PhotoUrl'])
        st.write('')  # Empty write calls are placeholders for potential additional content or spacing adjustments.


    # In the right column, display various pieces of information about the player, each as a separate markdown element for better formatting control.
    with col_right:
        # Display the ranking number and player name as a header.
        st.markdown(f"#### {i}. {rec_player}")
        # Display the player's market value, club, and key attributes such as overall rating, pace, shooting, etc.
        # Each attribute is displayed using markdown for consistent formatting.
        st.markdown(f"##### Value: {df.loc[rec_player]['ValueEUR']}")
        st.markdown(f"##### Club: {df.loc[rec_player]['Club']}")
        st.markdown(f"##### Overall: {df.loc[rec_player]['Overall']}")
        st.markdown(f"##### Pace: {df.loc[rec_player]['PaceTotal']}")
        st.markdown(f"##### Shooting: {df.loc[rec_player]['ShootingTotal']}")
        st.markdown(f"##### Passing: {df.loc[rec_player]['PassingTotal']}")
        st.markdown(f"##### Dribbling: {df.loc[rec_player]['DribblingTotal']}")
        st.markdown(f"##### Defending: {df.loc[rec_player]['DefendingTotal']}")
        st.markdown(f"##### Physicality: {df.loc[rec_player]['PhysicalityTotal']}")

    # After displaying each player's details, insert a horizontal rule (markdown) as a visual separator before moving on to the next player.
    st.markdown('***')