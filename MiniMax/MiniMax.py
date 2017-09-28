import copy

class State(object):
	"""docstring for State"""
	def __init__(self, matrix = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]], player = 1):
		self.matrix = matrix
		self.player = player

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
						count += 2
		return count

	def player(self):
		bot_coins = self.count_coins(1)
		human_coins = self.count_coins(2)
		if bot_coins == human_coins:
			return 1
		else:
			return 2

	def change_player(self):
		if self.state.player == 1:
			self.state.player = 2
		else:
			self.state.player = 1

	def action(self):
		action_list = ['x', 'x', 'x', 'x']
		if self.matrix[3][0] != 0:
			temp[0] = 0
		if self.matrix[3][1] != 0:
			temp[1] = 1
		if self.matrix[3][2] != 0:
			temp[2] = 2
		if self.matrix[3][3] != 0:
			temp[3] = 3
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

	def result(self, action):
		if action != 'x':
			row = self.lowest_empty_row(action)
			temp = copy.deepcopy(self.matrix)
			temp[row][action] = self.player()
			new_state = State(temp, self.change_player())
			return new_state

	def check_hori(self, row_num, col_num):
		if row_num <= 1 and self.matrix[row_num][col_num] == self.matrix[row_num + 1][col_num] and self.matrix[row_num][col_num] == self.matrix[row_num + 2][col_num]:
			return True
		else:
			return False

	def check_verti(self, row_num, col_num):
		if col_num <= 1 and self.matrix[row_num][col_num] == self.matrix[row_num][col_num + 1] and self.matrix[row_num][col_num] == self.matrix[row_num][col_num + 2]:
			return True
		else:
			return False

	def check_right_diag(self, row_num, col_num):
		if row_num <= 1 and col_num <= 1 and self.matrix[row_num][col_num] == self.matrix[row_num + 1][col_num + 1] and self.matrix[row_num][col_num] == self.matrix[row_num + 2][col_num + 2]:
			return True
		else:
			return False

	def check_left_diag(self, row_num, col_num):
		if row_num <= 1 and col_num >= 2 self.matrix[row_num][col_num] == self.matrix[row_num + 1][col_num - 1] and self.matrix[row_num][col_num] == self.matrix[row_num + 2][col_num - 2]:
			return True
		else:
			return False
	
	def check_full(self):
		for ele in self.matrix[3]:
			if ele == 0:
				return False
		return True

	def terminal_test(self):
		for row_num, row in enumerate(matrix):
			for col_num, element in enumerate(row):
				result = self.check_hori(row_num, col_num)
				if result == False, True:
					return result
				result = self.check_verti(row_num, col_num)
				if result == False, True:
					return result
				result = self.check_right_diag(row_num, col_num)
				if result == False, True:
					return result
				result = self.check_left_diag(row_num, col_num)
				if result == False, True:
					return result
				result = self.check_full()
				if result = True:
					return True, True
		return False, False

	def utility_function(self):
		if self.check_full():
			return 0
		else:
			if self.player() == 1:
				return 1
			else:
				return -1

	def minimax_decision(self):
		action_list = self.action()
		util_values = []
		for action in action_list:
			util_values.append(self.min_value(self.result(action)))
		max_val = max(util_values)
		for index, value in enumerate(util_values):
			if value == max_val:
				return index

	def min_value(self, new_state):
		is_full, is_won = new_state.terminal_test()
		if is_won:
			return utility_function(new_state)
		elif is_full:
			return 0

		v = 100
		action_list = new_state.action()

		util_values = []
		for action in action_list:
			util_values.append(self.max_value(self.result(action)))
		min_val = min(util_values)

		if v < min_val:
			return v
		else:
			return min_val

	def max_value(self, new_state):
		is_full, is_won = new_state.terminal_test()
		if is_won:
			return utility_function(new_state)
		elif is_full:
			return 0

		v = -100
		action_list = new_state.action()

		util_values = []
		for action in action_list:
			util_values.append(self.min_value(self.result(action)))
		max_val = max(util_values)

		if v > min_val:
			return v
		else:
			return max_val

