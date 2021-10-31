
# Custom imports
from multipage import MultiPage
from pages import player_comparison, main # import your pages here

# Create an instance of the app
app = MultiPage()


# Add all your application here
app.add_page("Main Page", main.app)
app.add_page("Player Comparison", player_comparison.app)


# The main app
app.run()