from GUI.GUI_init import *
from GUI.Screen_and_Click import *
from turtle import *

def main():
	screen, r_cood_list, gameplay_cood_list, grid_square_size, grid_start_coordinates, text_t, grid_t = initialise_board()
	click_action = CheckClick(gameplay_cood_list, grid_start_coordinates, grid_square_size, screen, grid_t, text_t)
	
	# fillCircles(grid_start_coordinates, grid_square_size, 1)

	screen.onclick(click_action.onclick_action)
	screen.listen()
		
	done()
	# screen.exitonclick()

if __name__ == "__main__":
	main()