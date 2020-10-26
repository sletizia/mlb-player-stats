from app.Player import Player
from app.SearchHelper import SearchHelper
from flask import Flask, render_template, request

app = Flask(__name__)
app.debug = True 

search_helper = SearchHelper()

@app.route('/')
def hello_world():
	# p = Player("alonso")
	# hr = p.hitting_stats[0]['stats']['homeRuns']
	return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
	if request.method == 'POST':
		search_name = request.form['name']
		player = Player(search_name)
		if player.exists:
			player_info = player.player_info
			# Maybe grab the team name and the position separatley so
			# as to send less data to the client (low coupling)
			if not player.hitting_stats:
				hitting_stats = None
			else:
				hitting_stats = player.hitting_stats[0]['stats']
			if not player.pitching_stats:
				pitching_stats = None
			else:
				pitching_stats = player.pitching_stats[0]['stats']
			if not player.fielding_stats:
				fielding_stats = None
			else:
				fielding_stats = player.fielding_stats[0]['stats']
			return render_template('statpage.html', player_info=player_info, hitting_stats = hitting_stats, pitching_stats=pitching_stats, fielding_stats=fielding_stats)
		else:
			# find a name similar to the one searcherd
			matches = search_helper.get_matches(search_name)
			return render_template('index.html', search_suggestions=matches)
