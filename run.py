##########################
# Abhishek V Joshi
# 2015A7PS0116P
##########################

from GUI.GUI_init import *
from GUI.Screen_and_Click import *
from turtle import *
from MinMax import *
from Alpha_Beta import *
from time import time

def main():
	screen, r_cood_list, gameplay_cood_list, grid_square_size, grid_start_coordinates, text_t, grid_t = initialise_board()
	fill_t = Turtle()
	fill_t.speed(0)
	# fillCircles(grid_start_coordinates, grid_square_size, 1)

	begin = myState()
	t0 = time()
	bot_action, temp_num_nodes, depth_of_stack = begin.minimax_decision()
	t1 = time()
	#GUI.Screen_and_Click.num_nodes_minimax += temp_num_nodes
	fillCircles(grid_start_coordinates, grid_square_size, 1, fill_t, [0, bot_action])
	next_state = begin.result(bot_action)
	
	text_t.penup()
	text_t.setpos(r_cood_list[1][0], r_cood_list[1][1])
	text_t.write(str(sys.getsizeof(myState())) + "Bytes", font = ("Arial", 15, "normal"))

	text_t.setpos(r_cood_list[2][0], r_cood_list[2][1])
	text_t.write(str(depth_of_stack), font = ("Arial", 15, "normal"))

	click_action = CheckClick(gameplay_cood_list, grid_start_coordinates, grid_square_size, screen, grid_t, text_t, fill_t, r_cood_list, next_state, temp_num_nodes)
	click_action.tot_time_minimax += t1 - t0
	screen.onclick(click_action.onclick_action)
	######## Enter the Ri printing code here.##########

	###################################################
	screen.listen()
		
	done()
	# screen.exitonclick()

if __name__ == "__main__":
	main()