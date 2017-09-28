from turtle import *
from GUI_init import *
import sys

class CheckClick(object):
	"""docstring for CheckClick"""

	# 0: drop coin in first column
	# 1: drop coin in second column
	# 2: drop coin in third column
	# 3: drop coin in fourth column
	# 4: new game initialised
	# 5: do nothing
	
	def __init__(self, gameplay_coordinates, grid_start_coordinates, grid_square_size, screen, grid_t, text_t):
		self.gameplay_coordinates = gameplay_coordinates
		self.grid_start_coordinates = grid_start_coordinates
		self.grid_square_size = grid_square_size
		self.screen = screen
		self.grid_t = grid_t
		self.text_t = text_t

	def new_game(self):
		height = float(self.screen.window_height())
		width = float(self.screen.window_width())
		self.text_t.clear()
		self.grid_t.clear()
		r_cood_list, gameplay_cood_list, self.text_t = show_text(width, height)
		self.grid_t = grid_init(self.grid_square_size, self.gameplay_coordinates[0][1], width, height, self.grid_start_coordinates)

	def check_click(self, x, y):
		if x > self.gameplay_coordinates[0][0] and x < self.gameplay_coordinates[1][0] and y > self.gameplay_coordinates[0][1] - 10 and y < self.gameplay_coordinates[0][1] + 20:
			return "new_game"			
		elif x > self.gameplay_coordinates[2][0] and x < self.gameplay_coordinates[3][0] and y > self.gameplay_coordinates[0][1] - 10 and y < self.gameplay_coordinates[0][1] + 20:
			return "exit"

		else:
			if y < self.grid_start_coordinates[1] and y > self.grid_start_coordinates[1] - (4 * self.grid_square_size):
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
		result = self.check_click(x, y)
		if result == "new_game":
			self.new_game()
		elif result == "exit":
			sys.exit()
		elif result == "do_nothing":
			pass
		else:
			print(result)

