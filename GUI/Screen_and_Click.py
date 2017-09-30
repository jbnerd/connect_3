from turtle import *
from GUI.GUI_init import *
import sys

sys.path.insert(0, '/home/jbnerd/AI_assignment2/MiniMax')
from MinMax import *
from Alpha_Beta import *

class CheckClick(object):
	"""docstring for CheckClick"""

	# 0: drop coin in first column
	# 1: drop coin in second column
	# 2: drop coin in third column
	# 3: drop coin in fourth column
	# 4: new game initialised
	# 5: do nothing
	def __init__(self, gameplay_coordinates, grid_start_coordinates, grid_square_size, screen, grid_t, text_t, fill_t, r_cood_list, state, alphabeta = 0):
		self.gameplay_coordinates = gameplay_coordinates
		self.grid_start_coordinates = grid_start_coordinates
		self.grid_square_size = grid_square_size
		self.screen = screen
		self.grid_t = grid_t
		self.text_t = text_t
		self.fill_t = fill_t
		self.r_cood_list = r_cood_list
		self.state = state
		self.alphabeta = alphabeta
		self.game_over = 0

	def reinitialise_board(self):
		height = float(self.screen.window_height())
		width = float(self.screen.window_width())

		#clearing the board
		self.text_t.clear()
		self.grid_t.clear()
		self.fill_t.clear()

		# Initialsing GUI
		self.r_cood_list, self.gameplay_cood_list, self.text_t = show_text(width, height)
		self.grid_t = grid_init(self.grid_square_size, self.gameplay_coordinates[0][1], width, height, self.grid_start_coordinates)

	def check_click(self, x, y, game_over = 0):
		if x > self.gameplay_coordinates[0][0] and x < self.gameplay_coordinates[1][0] and y > self.gameplay_coordinates[0][1] - 10 and y < self.gameplay_coordinates[0][1] + 20:
			return "new_game_slow"			
		elif x > self.gameplay_coordinates[2][0] and x < self.gameplay_coordinates[3][0] and y > self.gameplay_coordinates[0][1] - 10 and y < self.gameplay_coordinates[0][1] + 20:
			return "new_game_fast"
		elif x > self.gameplay_coordinates[4][0] and x < self.gameplay_coordinates[5][0] and y > self.gameplay_coordinates[0][1] - 10 and y < self.gameplay_coordinates[0][1] + 20:
			return "exit"
		elif self.game_over == 0 and y < self.grid_start_coordinates[1] and y > self.grid_start_coordinates[1] - (4 * self.grid_square_size):
			if x > self.grid_start_coordinates[0] and x < self.grid_start_coordinates[0] + self.grid_square_size:
				return 0
			elif x > self.grid_start_coordinates[0] + self.grid_square_size and x < self.grid_start_coordinates[0] + (2 * self.grid_square_size):
				return 1
			elif x > self.grid_start_coordinates[0] + (2 * self.grid_square_size) and x < self.grid_start_coordinates[0] + (3 * self.grid_square_size):
				return 2
			elif x > self.grid_start_coordinates[0] + (3 * self.grid_square_size) and x < self.grid_start_coordinates[0] + (4 * self.grid_square_size):
				return 3
		else:
			return "do_nothing"

	def onclick_action(self, x, y):
		click_pos = self.check_click(x, y, self.game_over)
		if click_pos == "exit":
			sys.exit()
		elif click_pos == "new_game_fast":
			self.reinitialise_board()
			self.state = State()
			self.alphabeta = 1
			self.game_over = 0
		elif click_pos == "new_game_slow":
			self.reinitialise_board()
			self.state = myState()
			self.alphabeta = 0
			self.game_over = 0
		elif (click_pos == 0 or click_pos == 1 or click_pos == 2 or click_pos == 3) and self.game_over == 0:
			# print(click_pos, self.state.lowest_empty_row(click_pos))
			fillCircles(self.grid_start_coordinates, self.grid_square_size, 2, self.fill_t, [self.state.lowest_empty_row(click_pos), click_pos])
			self.state = self.state.result(click_pos)
			# print(self.state)
		else:
			pass

		if self.game_over == 0:
			if self.alphabeta == 0:
				bot_action = self.state.minimax_decision()
				fillCircles(self.grid_start_coordinates, self.grid_square_size, 1, self.fill_t, [self.state.lowest_empty_row(bot_action), bot_action])
				self.state = self.state.result(bot_action)
				is_full, is_won = self.state.terminal_test()
				if is_won:
					print("Bot Wins")
					self.game_over = 1
					# sys.exit()
				elif is_full:
					print("Game is Draw")
					self.game_over = 1
					# sys.exit()
			else:
				bot_action = self.state.alpha_beta_search()
				if bot_action >= 0 and bot_action < 4:
					fillCircles(self.grid_start_coordinates, self.grid_square_size, 1, self.fill_t, [self.state.lowest_empty_row(bot_action), bot_action])
					self.state = self.state.result(bot_action)
					is_full, is_won = self.state.terminal_test()
					if is_won:
						print("Bot Wins")
						self.game_over = 1
					elif is_full:
						print("Game is Draw")
						self.game_over = 1


