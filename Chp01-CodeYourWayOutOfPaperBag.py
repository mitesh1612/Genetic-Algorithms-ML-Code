import turtle as t
import pickle
import random

def drawBag():
	'''
	Method to draw the paper bag
	'''
	t.shape('turtle')
	# Set pen for the brown bag
	t.pen(pencolor = 'brown', pensize = 5)
	# Put the pen up to move the t to the start position
	t.penup()
	t.goto(-35, 35)
	# Putting the pen down
	t.pendown()
	t.right(90)
	t.forward(70)
	t.left(90)
	t.forward(70)
	t.left(90)
	t.forward(70)

def escaped(position):
	'''
	Check whether the turtle is out of the bag or not
	Since bag starts at x=-35 to x=35 and is 70 units across
	And y=-35 to y=35 and is 70 units high
	'''
	x = int(position[0])
	y = int(position[1])
	return x < -35 or x > 35 or y < -35 or y > 35

def drawLine():
	'''
	Set the turtle off and keep going until he is out
	'''
	angle = 0
	step = 5
	turt = t.Turtle()
	while not escaped(turt.position()):
		turt.left(angle)
		turt.forward(step)

def storePositionData(L, turt):
	'''
	Store the position data of the turtle, incl whether its in or out of paper bag
	'''
	position = turt.position()
	L.append([position[0], position[1], escaped(position)])

def drawSquare(turt, size):
	'''
	To escape using squares. For this the turtle needs to increase the size as he goes
	As squares get bigger, it'll get nearer to the edges of the paper bag, eventually going through it
	'''
	L = []
	# To draw a square, move forward and turn a right angle four times
	for i in range(4):
		turt.forward(size)
		turt.left(90)
		storePositionData(L, turt)
	return L

def drawSquares(number):
	'''
	Draw a given number of squares
	'''
	turt = t.Turtle()
	L = []
	for i in range(1, number+1):
		turt.penup()
		turt.goto(-i, -i)
		turt.pendown()
		L.extend(drawSquare(turt, i*2))
	return L

def drawSquaresUntilEscapes(n):
	'''
	Store the data of L positions
	'''
	turt = t.Turtle()
	L = drawSquares(n)
	with open("data_square", "wb") as f:
		pickle.dump(L, f)

def drawTriangles(number):
	'''
	Draw Spirangles in Triangle Shape
	'''
	turt = t.Turtle()
	for i in range(1, number):
		turt.forward(i*10)
		turt.right(120)

def drawSpiralsUntilEscaped():
	'''
	Draw Spirangles using random angles until the turtle escapes
	'''
	turt = t.Turtle()
	turt.penup()
	turt.left(random.randint(0, 360))
	turt.pendown()
	i = 0
	turn = 360/random.randint(1, 10)
	L = []
	storePositionData(L, turt)
	while not escaped(turt.position()):
		i += 1
		turt.forward(i*5)
		turt.right(turn)
		storePositionData(L, turt)
	return L

if __name__ == '__main__':
	# Set the window size : set it something larger than paper bag otherwise wont be able to see bag
	t.setworldcoordinates(-70., -70., 70., 70.)
	drawBag()
	# To Draw Lines
	# drawLine()
	# To Draw squares
	# drawSquares(50)
	# To Draw Triangles
	# drawTriangles(10)
	# To Draw Spirangles
	drawSpiralsUntilEscaped()
	# To keep the turtle window open
	t.mainloop()


