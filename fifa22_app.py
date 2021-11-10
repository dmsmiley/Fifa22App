
# Custom imports
from multipage import MultiPage
from pages import player_comparison, main, team_distribution, player_recommendation, custom_recommender # import your pages here

# Create an instance of the app
app = MultiPage()

# Add all your application here
app.add_page("Main Page", main.app)
app.add_page("Player Recommendation", player_recommendation.app)
app.add_page("Player Comparison", player_comparison.app)
app.add_page("League Distribution", team_distribution.app)
app.add_page("Custom Recommender", custom_recommender.app)

# The main app
app.run()