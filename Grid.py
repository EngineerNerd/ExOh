def sign(x):
    if x > 0:
        return 'positive'
    elif x < 0:
        return 'negative'
    else:
        return 'zero'


def duck():
	print("ducks are cute")
	

def printGrid():
	print("positions on grid:")
	print('%d | %d | %d' % (0, 1, 2))
	print("-   -   -")
	print('%d | %d | %d' % (3, 4, 5))
	print("-   -   -")
	print('%d | %d | %d' % (6, 7, 8))


printGrid()