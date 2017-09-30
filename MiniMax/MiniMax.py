import copy

class State(object):
	"""docstring for State"""
	def __init__(self, matrix = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]], player = 1):
		self.matrix = matrix
		self.player = player

	def __eq__(self, other):
		return self.matrix == other.matrix and self.player == other.player

	def __ne__(self, other):
		return not self.__eq__(other)

	def __str__(self):
		if self.player == 1:
			return str(self.matrix[0]) + "\n" + str(self.matrix[1]) + "\n" + str(self.matrix[2]) + "\n" + str(self.matrix[3]) + "\n Bot's Turn"
		else:
			return str(self.matrix[0]) + "\n" + str(self.matrix[1]) + "\n" + str(self.matrix[2]) + "\n" + str(self.matrix[3]) + "\n Player's Turn"

	def __repr__(self):
		return str(self.matrix)

	def __hash__(self):
		return hash(tuple([tuple(x) for x in self.matrix]))

	def count_coins(self, player_num):
		count = 0
		if player_num == 1:
			for i in self.matrix:
				for j in i:
					if j == 1:
						count += 1
		else:
			for i in self.matrix:
				for j in i:
					if j == 2:
						count += 1
		return count

	def player_turn(self):
		bot_coins = self.count_coins(1)
		human_coins = self.count_coins(2)
		if bot_coins == human_coins:
			return 1
		else:
			return 2

	def change_player(self):
		if self.player == 1:
			return 2
		else:
			return 1

	def action(self):
		action_list = ['x', 'x', 'x', 'x']
		if self.matrix[3][0] == 0:
			action_list[0] = 0
		if self.matrix[3][1] == 0:
			action_list[1] = 1
		if self.matrix[3][2] == 0:
			action_list[2] = 2
		if self.matrix[3][3] == 0:
			action_list[3] = 3
		return action_list

	def lowest_empty_row(self, col):
		if self.matrix[0][col] == 0:
			return 0
		elif self.matrix[1][col] == 0:
			return 1
		elif self.matrix[2][col] == 0:
			return 2
		elif self.matrix[3][col] == 0:
			return 3
		else:
			return -1

	def result(self, action):
		if action != 'x':
			row = self.lowest_empty_row(action)
			temp = copy.deepcopy(self.matrix)
			temp[row][action] = self.player_turn()
			new_state = State(matrix = temp, player = self.change_player())
			return new_state

	def check_verti(self, row_num, col_num):
		if self.matrix[row_num][col_num] != 0 and row_num <= 1 and self.matrix[row_num][col_num] == self.matrix[row_num + 1][col_num] and self.matrix[row_num][col_num] == self.matrix[row_num + 2][col_num]:
			return True
		else:
			return False

	def check_hori(self, row_num, col_num):
		if self.matrix[row_num][col_num] != 0 and col_num <= 1 and self.matrix[row_num][col_num] == self.matrix[row_num][col_num + 1] and self.matrix[row_num][col_num] == self.matrix[row_num][col_num + 2]:
			return True
		else:
			return False

	def check_right_diag(self, row_num, col_num):
		if self.matrix[row_num][col_num] != 0 and row_num <= 1 and col_num <= 1 and self.matrix[row_num][col_num] == self.matrix[row_num + 1][col_num + 1] and self.matrix[row_num][col_num] == self.matrix[row_num + 2][col_num + 2]:
			return True
		else:
			return False

	def check_left_diag(self, row_num, col_num):
		if self.matrix[row_num][col_num] != 0 and row_num <= 1 and col_num >= 2 and self.matrix[row_num][col_num] == self.matrix[row_num + 1][col_num - 1] and self.matrix[row_num][col_num] == self.matrix[row_num + 2][col_num - 2]:
			return True
		else:
			return False
	
	def check_full(self):
		for ele in self.matrix[3]:
			if ele == 0:
				return False
		return True

	def terminal_test(self):
		is_full = False
		is_won = False
		for row_num, row in enumerate(self.matrix):
			for col_num, element in enumerate(row):
				result = self.check_hori(row_num, col_num)
				if result == True:
					# print("hori")
					is_won = True
					# return False, result
				else:
					result = self.check_verti(row_num, col_num)
					if result == True:
						# print("verti")
						is_won = True
						# return False, result
					else:
						result = self.check_right_diag(row_num, col_num)
						if result == True:
							# print("rigth_diag")
							is_won = True
							# return False, result
						else:
							result = self.check_left_diag(row_num, col_num)
							if result == True:
								# print("left_diag")
								is_won = True
								# return False, result
							else:
								result = self.check_full()
								if result == True:
									# print("full")
									is_full = True
									# return True, True
		# return False, False
		return is_full, is_won

	def utility_function(self):
		if self.check_full():
			return 0
		else:
			if self.player_turn() == 1:
				return -1
			else:
				return 1

	def minimax_decision(self):
		action_list = self.action()
		util_values = {}
		explored = {}
		for action in action_list:
			temp = self.result(action)
			if temp is not None:
				# print(temp)
				util_values[action] = min_value(temp, explored)
		# print("-------------------------")
		# print(util_values)
		max_val = -100
		action = -1
		for act, util_value in util_values.items():
			if max_val < util_value:
				max_val = util_value
				action = act
		return action

def min_value(state, explored):
	is_full, is_won = state.terminal_test()
	if is_won:
		# print("terminal test: " + str(state.utility_function()))
		return state.utility_function()
	elif is_full:
		return 0

	v = 100
	action_list = state.action()

	util_values = []
	for action in action_list:
		temp = state.result(action)
		if temp is not None and temp not in explored:
			# print(temp)
			maxi = max_value(temp, explored)
			util_values.append(maxi)
			explored[temp] = maxi
		elif temp is not None:
			util_values.append(explored[temp])
	# print("------------------------------------------------------------")
	min_val = min(util_values)

	if v < min_val:
		return v
	else:
		return min_val

def max_value(state, explored):
	is_full, is_won = state.terminal_test()
	if is_won:
		return state.utility_function()
	elif is_full:
		return 0

	v = -100
	action_list = state.action()

	util_values = []
	for action in action_list:
		temp = state.result(action)
		if temp is not None and temp not in explored:
			# print(temp)
			mini = min_value(temp, explored)
			util_values.append(mini)
			explored[temp] = mini
		elif temp is not None:
			util_values.append(explored[temp])
	# print("------------------------------------------------------------")
	max_val = max(util_values)

	if v > max_val:
		return v
	else:
		return max_val

def start_game_minimax():
	begin = State()
	state = begin
	while True:
		bot_action = state.minimax_decision()
		next_state = state.result(bot_action)
		print(next_state)
		is_full, is_won = next_state.terminal_test()
		if is_full or is_won:
			print("Bot wins")
			break
		human_action = raw_input()
		human_action = int(human_action)
		state = next_state.result(human_action)
		print(state)

		
	
if __name__ == "__main__":
	start_game_minimax()