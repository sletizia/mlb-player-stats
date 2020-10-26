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
		self.player_info = self.__get_player_info()
		if self.player_info == None:
			self.exists = False
		else:
			self.exists = True
			self.player_id = self.player_info['id']
			self.player_stat_data = self.__get_player_stats()
			self.team_id = self.player_info['currentTeam']['id']

			self.hitting_stats, self.fielding_stats, self.pitching_stats = self.__set_stats()

	def get_search_name(self):
		return self.search_name

	def __get_player_info(self):
		# Returns a dictionary of player info from the stats api
		stats = statsapi.lookup_player(self.search_name)
		if stats:
			return stats[0]
		else:
			return None
	def __get_player_stats(self):
		# Returns a dictionary of player stats from the stats api
		return statsapi.player_stat_data(self.player_id)

	def __set_stats(self):
		hitting_stats = []
		fielding_stats = []
		pitching_stats = []
		for category in self.player_stat_data['stats']:
			if category['group'] == 'hitting':
				hitting_stats.append(category)
			elif category['group'] == 'fielding':
				fielding_stats.append(category)
			elif category['group'] == 'pitching':
				pitching_stats.append(category)
		
		return hitting_stats, fielding_stats, pitching_stats



if __name__ == '__main__':
	degrom = Player("degrom")
	print(degrom.pitching_stats[0]['stats']['strikeOuts'])

	


