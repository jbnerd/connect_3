from GUI.GUI_init import *
from GUI.Screen_and_Click import *
from turtle import *
from MinMax import *
from Alpha_Beta import *

def main():
	screen, r_cood_list, gameplay_cood_list, grid_square_size, grid_start_coordinates, text_t, grid_t = initialise_board()
	fill_t = Turtle()
	fill_t.speed(0)
	# fillCircles(grid_start_coordinates, grid_square_size, 1)

	begin = myState()
	bot_action = begin.minimax_decision()
	fillCircles(grid_start_coordinates, grid_square_size, 1, fill_t, [0, bot_action])
	next_state = begin.result(bot_action)

	click_action = CheckClick(gameplay_cood_list, grid_start_coordinates, grid_square_size, screen, grid_t, text_t, fill_t, r_cood_list, next_state)
	screen.onclick(click_action.onclick_action)
	screen.listen()
		
	done()
	# screen.exitonclick()

if __name__ == "__main__":
	main()