def sign(x):
    if x > 0:
        return 'positive'
    elif x < 0:
        return 'negative'
    else:
        return 'zero'


def duck():
	print("ducks are cute")
	

def printGridPositions():
	print("positions on grid:")
	print('%d | %d | %d' % (0, 1, 2))
	print("-   -   -")
	print('%d | %d | %d' % (3, 4, 5))
	print("-   -   -")
	print('%d | %d | %d' % (6, 7, 8))


def printGridEmpty():
	print("empty grid:")
	print("  |   |  ")
	print("-   -   -")
	print("  |   |  ")
	print("-   -   -")
	print("  |   |  ")


def printGridExample():
	print("an example game:")
	print('%c | %c | %c' % ('X', 'O', 'O'))
	print("-   -   -")
	print('%c | %c | %c' % ('O', 'X', 'X'))
	print("-   -   -")
	print('%c | %c | %c' % ('X', 'O', 'O'))


def printGridGame(zero, one, two, three, four, five, six, seven, eight):
	print("the game so far:")
	print( "{} | {} | {}".format(zero, one, two) )
	print("-   -   -")
	print( "{} | {} | {}".format(three, four, five) )
	print("-   -   -")
	print( "{} | {} | {}".format(six, seven, eight) )

if __name__ == "__main__":
	
	print( "Hello {} {}".format("World", "Helen") )
	
	printGridPositions()
	printGridEmpty()
	printGridExample()
	
	printGridGame(" ", " ", "O", "O", " ", " ", "X", " ", "O")
	printGridGame("X", "O", "O", "O", "X", "X", "X", "O", "O")
	
	pass
