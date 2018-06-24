from Grid import *


number = -2

print(sign(number)) 


gametest = {0: " ", 1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " "}


game = [[0,1,2],
	   [3,4,5],
       [6,7,8]]

	   
"""

print("\n")
	   
print(game)
game[0][0]=gametest[0]
print("\n")
	   
print(game)


inputfromuser = input("Where would you like to move?")
print(inputfromuser)
print("\n")
if inputfromuser == "1":
	print("True")
	game[0][1]= "X"
else:
	print ("False")
		
print(game)

""" 
"""
for i in range(9):
	inputfromuser = input("Where would you like to move?")

	gametest[int(inputfromuser)] = "X"

	print(gametest)
	
	
	""" 

	
	
for i in range(9):	
	printGridGame(gametest[0],gametest[1],gametest[2],gametest[3],gametest[4],gametest[5],gametest[6],gametest[7],gametest[8])
	inputfromuser = input("Player 1: Where would you like to move?")	
	gametest[int(inputfromuser)] = "X"	
	printGridGame(gametest[0],gametest[1],gametest[2],gametest[3],gametest[4],gametest[5],gametest[6],gametest[7],gametest[8])
	inputfromuser = input("Plaer 2: Where would you like to move?")	
	gametest[int(inputfromuser)] = "O"	
	printGridGame(gametest[0],gametest[1],gametest[2],gametest[3],gametest[4],gametest[5],gametest[6],gametest[7],gametest[8])

 

 
#sdahkllfsjklsd 
 
duck()


#dffdfafasdf

