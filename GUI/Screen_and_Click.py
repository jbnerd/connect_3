from turtle import *
from GUI.GUI_init import *
import sys
from time import time

sys.path.insert(0, '/home/jbnerd/AI_assignment2/MiniMax')
from MinMax import *
from Alpha_Beta import *

M_wins_ten_times = 0
avg_M_wins_ten_times = 10


class CheckClick(object):
	"""docstring for CheckClick"""

	# 0: drop coin in first column
	# 1: drop coin in second column
	# 2: drop coin in third column
	# 3: drop coin in fourth column
	# 4: new game initialised
	# 5: do nothing
	def __init__(self, gameplay_coordinates, grid_start_coordinates, grid_square_size, screen, grid_t, text_t, fill_t, r_cood_list, state, num_nodes_minimax, alphabeta = 0):
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
		self.game_one = 1
		self.alpha_game_one = 0
		self.alpha_game_one_check = 0
		self.num_nodes_minimax = num_nodes_minimax
		self.tot_time_minimax = 0
		self.num_nodes_alpha_beta = 0
		self.tot_time_alpha_beta = 0
		self.tot_time_ten_times = 0
		self.num_minimax_games = 0

	def reinitialise_board(self):
		height = float(self.screen.window_height())
		width = float(self.screen.window_width())

		#clearing the board
		# self.text_t.clear()
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
			self.num_nodes_alpha_beta = 0
			self.tot_time_alpha_beta = 0
			if self.alpha_game_one_check == 0:
				self.alpha_game_one = 1
				self.alpha_game_one_check = 1
			else:
				self.alpha_game_one = 0
		elif click_pos == "new_game_slow":
			self.reinitialise_board()
			self.state = myState()
			self.alphabeta = 0
			self.game_over = 0
			self.game_one = 0
			self.num_nodes_minimax = 0
			self.tot_time_minimax = 0
		elif (click_pos == 0 or click_pos == 1 or click_pos == 2 or click_pos == 3) and self.game_over == 0:
			# print(click_pos, self.state.lowest_empty_row(click_pos))
			fillCircles(self.grid_start_coordinates, self.grid_square_size, 2, self.fill_t, [self.state.lowest_empty_row(click_pos), click_pos])
			self.state = self.state.result(click_pos)
			# print(self.state)
		else:
			pass

		if self.game_over == 0:
			if self.alphabeta == 0:
				t0 = time()
				bot_action, temp_num_nodes_minimax, garbage = self.state.minimax_decision()
				t1 = time()
				self.tot_time_minimax += t1 - t0
				# print(self.tot_time_minimax)

				self.num_nodes_minimax += temp_num_nodes_minimax
				fillCircles(self.grid_start_coordinates, self.grid_square_size, 1, self.fill_t, [self.state.lowest_empty_row(bot_action), bot_action])
				self.state = self.state.result(bot_action)
				is_full, is_won = self.state.terminal_test()
				if is_won:
					print("Bot Wins")
					self.game_over = 1
					if self.num_minimax_games <= 9:
						self.tot_time_ten_times += self.tot_time_minimax
						self.num_minimax_games += 1

					if self.num_minimax_games == 10:
						avg = float(self.tot_time_ten_times)/self.num_minimax_games
						self.text_t.penup()
						self.text_t.setpos(self.r_cood_list[9][0], self.r_cood_list[9][1])
						self.text_t.write(str(avg), font = ("Arial", 15, "normal"))

						self.text_t.setpos(self.r_cood_list[10][0], self.r_cood_list[10][1])
						self.text_t.write(str(10), font = ("Arial", 15, "normal"))

						self.text_t.setpos(self.r_cood_list[11][0], self.r_cood_list[11][0])
						self.text_t.write(str(10), font = ("Arial", 15, "normal"))

					if self.game_one == 1:
						self.text_t.penup()
						self.text_t.setpos(self.r_cood_list[0][0], self.r_cood_list[0][1])
						self.text_t.write(str(self.num_nodes_minimax), font = ("Arial", 15, "normal"))

						self.text_t.setpos(self.r_cood_list[3][0], self.r_cood_list[3][1])
						self.text_t.write(str(round(self.tot_time_minimax, 4)) + " seconds", font = ("Arial", 15, "normal"))

						num_nodes_micro = self.num_nodes_minimax/(self.tot_time_minimax * 1000000)
						self.text_t.setpos(self.r_cood_list[4][0], self.r_cood_list[4][1])
						self.text_t.write(str(num_nodes_micro), font = ("Arial", 15, "normal"))
						self.game_one = 0

				elif is_full:
					print("Game is Draw")
					self.game_over = 1
			else:
				t0 = time()
				bot_action, temp_num_nodes_alpha_beta = self.state.alpha_beta_search()
				t1 = time()
				self.tot_time_alpha_beta += t1 - t0

				self.num_nodes_alpha_beta += temp_num_nodes_alpha_beta
				if bot_action >= 0 and bot_action < 4:
					fillCircles(self.grid_start_coordinates, self.grid_square_size, 1, self.fill_t, [self.state.lowest_empty_row(bot_action), bot_action])
					self.state = self.state.result(bot_action)
					is_full, is_won = self.state.terminal_test()
					if is_won:
						print("Bot Wins")
						self.game_over = 1

						if self.alpha_game_one == 1:
							self.text_t.penup()
							self.text_t.setpos(self.r_cood_list[5][0], self.r_cood_list[5][1])
							self.text_t.write(str(self.num_nodes_alpha_beta), font = ("Arial", 15, "normal"))

							# print(self.num_nodes_minimax, self.num_nodes_alpha_beta)
							r7 = float(self.num_nodes_minimax - self.num_nodes_alpha_beta)/self.num_nodes_minimax
							# print(float(self.num_nodes_minimax - self.num_nodes_alpha_beta)/self.num_nodes_minimax)
							self.text_t.setpos(self.r_cood_list[6][0], self.r_cood_list[6][1])
							self.text_t.write(str(r7), font = ("Arial", 15, "normal"))

							self.text_t.setpos(self.r_cood_list[7][0], self.r_cood_list[7][1])
							self.text_t.write(str(self.tot_time_alpha_beta) + " seconds", font = ("Arial", 15, "normal"))

							mem_minimax = self.num_nodes_minimax * 64
							mem_alpha_beta = self.num_nodes_alpha_beta * 64
							self.text_t.setpos(self.r_cood_list[8][0], self.r_cood_list[8][1])
							self.text_t.write(str(mem_minimax) + ", " + str(mem_alpha_beta), font = ("Arial", 15, "normal"))

							self.alpha_game_one = 0
			
					elif is_full:
						print("Game is Draw")
						self.game_over = 1


