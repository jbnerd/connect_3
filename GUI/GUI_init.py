from turtle import *

def show_text(width, height):
	text_t = Turtle()
	text_t.penup()
	text_t.speed(0)
	text_t.ht()
	text_t.setpos((width/3)-(width/2), (-1 * height)/2)
	text_t.pendown()
	text_t.left(90)
	text_t.pensize(3)
	text_t.fd(height)
	text_t.penup()

	text_t.setpos(-1 * width/2 + 10, height/2 - 50)
	r_cood_list = []
	for i in range(1, 13):
		text_t.write("R" + str(i) + " :", move = True, font = ("Arial", 15, "normal"))
		temp = text_t.pos()
		r_cood_list.append(temp)
		text_t.penup()
		text_t.setpos(-1 * width/2 + 10, temp[1] - height/13)

	gameplay_cood_list = []
	text_t.setpos(90, (-1 * height)/2 + 50)
	start1 = (90, (-1 * height)/2 + 50)
	gameplay_cood_list.append(start1)
	text_t.write("New Game", move = True, font = ("Arial", 15, "bold"))
	gameplay_cood_list.append(text_t.pos())
	start2 = text_t.pos()[0] + 30, text_t.pos()[1]
	gameplay_cood_list.append(start2)
	text_t.setpos(text_t.pos()[0] + 30, text_t.pos()[1])
	text_t.write("Exit", move = True, font = ("Arial", 15, "bold"))
	gameplay_cood_list.append(text_t.pos())

	return r_cood_list, gameplay_cood_list, text_t

def grid_init(grid_square_size, hori_line_y_coordinate, width, height, coordinates):
	grid_t = Turtle()
	grid_t.penup()
	grid_t.speed(0)
	grid_t.setpos((width/3)-(width/2), hori_line_y_coordinate + 50)
	grid_t.pendown()
	grid_t.pensize(3)
	grid_t.fd(2*width/3)

	grid_t.pensize(1.5)
	grid_t.penup()
	grid_t.setpos(coordinates[0], coordinates[1])
	# grid_t.right(90)

	for i in range(6):
		grid_t.pendown()
		grid_t.fd(4*grid_square_size)
		grid_t.penup()
		grid_t.setpos(coordinates[0], coordinates[1] - i*grid_square_size)

	grid_t.right(90)
	grid_t.penup()
	grid_t.setpos(coordinates[0], coordinates[1])
	
	for i in range(6):
		grid_t.pendown()
		grid_t.fd(4*grid_square_size)
		grid_t.penup()
		grid_t.setpos(coordinates[0] + i*grid_square_size, coordinates[1])

	grid_t.penup()
	grid_t.right(180)

	return grid_t

def initialise_board():
	screen = Screen()
	screen.title("\t"*11 + "Align-3")

	height = float(screen.window_height())
	width = float(screen.window_width())
	print(width, height)

	r_cood_list, gameplay_cood_list, text_t = show_text(width, height)
	# print(r_cood_list)
	print(gameplay_cood_list)

	grid_square_size = ((2*width/3) - 40)/4
	grid_start_coordinates = [(width/3)-(width/2) + 20, height/2 - 40]
	print(grid_start_coordinates)
	print(grid_square_size)
	grid_t = grid_init(grid_square_size, gameplay_cood_list[0][1], width, height, grid_start_coordinates)
	# done()

	return screen, r_cood_list, gameplay_cood_list, grid_square_size, grid_start_coordinates, text_t, grid_t

def fillCircles(grid_coordinate, grid_square_size, minmax):
	fill_t = Turtle()
	fill_t.penup()
	fill_t.setpos(grid_coordinate[0] + grid_square_size/2, grid_coordinate[1] - grid_square_size)
	if minmax == 0:
		fill_t.color("black", "green")
	else:
		fill_t.color("black", "blue")
	fill_t.pendown()
	fill_t.pensize(2)
	fill_t.begin_fill()
	fill_t.circle(grid_square_size/2)
	fill_t.end_fill()
