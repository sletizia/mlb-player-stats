from app.Player import Player
from app.SearchHelper import SearchHelper
from flask import Flask, render_template, request

app = Flask(__name__)
app.debug = True 

search_helper = SearchHelper()

@app.route('/')
def home():
	# Route for the home view
	return render_template('index.html')

@app.route('/stats', methods=['POST'])
def submit():
	# Route for the statistics view
	# Either displays stats or re-renders index page with search suggestions
	if request.method == 'POST':
		search_name = request.form['name']
		player = Player(search_name)
		if player.exists:
			# Display the stats
			return render_template('statpage.html', player=player)
		else:
			# Use the SearchHelper to find potential matches
			matches = search_helper.get_matches(search_name)
			return render_template('index.html', search_suggestions=matches)
