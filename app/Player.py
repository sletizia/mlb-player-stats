import statsapi

class Player(object):
	"""
	Player object containes the methods to retrieve a players stats
	and info from the MLB statsapi.

	Uses package statsapi. 
	Docs here: https://github.com/toddrob99/MLB-StatsAPI/wiki

	Needs a string argument of the players last, or first and last
	name. ex: 'degrom' or 'todd frazier'
	"""
	def __init__(self, search_name):
		super(Player, self).__init__()
		self.search_name = search_name
		self.player_info = self.__get_player_info(search_name)
		if self.player_info == None:
			self.exists = False
		else:
			self.exists = True
			self.player_id = self.player_info['id']
			self.player_stat_data = self.__get_player_stats()
			self.team_id = self.player_info['currentTeam']['id']
			self.team_info = self.__get_team_info()
			self.team_colors = self.__get_team_color_class_names()
			self.hitting_stats, self.fielding_stats, self.pitching_stats = self.__set_stats()


	def __get_player_info(self, search_name):
		# Takes the search_name
		# Returns a dictionary of player info from the stats api or None
		stats = statsapi.lookup_player(search_name)
		if stats:
			return stats[0]
		else:
			return None
	def __get_player_stats(self):
		# Returns a dictionary of player stats from the stats api
		return statsapi.player_stat_data(self.player_id)

	def __set_stats(self):
		# Extracts the hitting, fielding, and pitching stats from the greater
		# player_stat_data object
		# returns three dictionaries
		hitting_stats = []
		fielding_stats = []
		pitching_stats = []
		for category in self.player_stat_data['stats']:
			# Check the players stat data for existence of the various
			# stat categories (all pithcers don't have hitting stats,
			# some position players may have pitching stats etc)
			if category['group'] == 'hitting':
				hitting_stats.append(category)
			elif category['group'] == 'fielding':
				fielding_stats.append(category)
			elif category['group'] == 'pitching':
				pitching_stats.append(category)
		# Extract the 'stats' section from the player_stat_data which
		# contains other info that we don't need 
		if hitting_stats:
			hitting_stats = hitting_stats[0]['stats']
		if fielding_stats:
			fielding_stats = fielding_stats[0]['stats']
		if pitching_stats:
			pitching_stats = pitching_stats[0]['stats']
		return hitting_stats, fielding_stats, pitching_stats
	
	def __get_team_info(self):
		# Use the team id to get the players team info
		# returns the dictionary of team info from the stats api
		team_id = self.player_info["currentTeam"]["id"]
		team_info = statsapi.lookup_team(team_id)
		return(team_info)
	
	def __get_team_color_class_names(self):
		# Uses the team name to generate the CSS class names of the teams colors
		# returns a two element list ["mets0", "mets1"]
		team_name = self.team_info[0]["teamName"].lower()
		return([team_name.replace(" ", "") + "0", team_name.replace(" ", "") + "1"])
		
		



if __name__ == '__main__':
	degrom = Player("degrom")
	print(degrom.get_team_colors())

	


