import sys
import os
import time
###
import checkConstraintfinal1
import position
import AI

def Instructions(player):
	os.system('clear')

	if player == "two_pl":

		print """

INSTRUCTIONS:
------------

1.) Choose the symbol 'X' or 'O' for each player.
2.) Each time players will be prompted to choose the square to place their symbol.
3.) A vertical and horizontal grid scale will be displayed along side left and top of the board respectively.
	Enter the appropraite position.
			For Example

		  +-----+-----+------+
		  +     +     +      +
		  +  1  +  2  +   3  +
		  +-----+-----+------+
		  +     +     +      +
		  +  4  +  5  +   6  +
		  +-----+-----+------+
		  +     +     +      +
		  +  7  +  8  +   9  +
		  +-----+-----+------+ 

		   Type the number in appropriate boxes when prompted

4.) A player wins when their symbol is in three consecutive boxes wether vertical or horizontal or diagonally present.
5.) Enjoy the game
		"""
		if raw_input() == "":
			pass

	elif player == "one_pl":

		print """

INSTRUCTIONS:
------------

1.) Choose the symbol 'X' or 'O'.
2.) Each time player will be prompted to choose the square to place your symbol.
3.) A vertical and horizontal grid scale will be displayed along side left and top of the board respectively.
	Enter the appropraite position.
			For Example

		  +-----+-----+------+
		  +     +     +      +
		  +  1  +  2  +   3  +
		  +-----+-----+------+
		  +     +     +      +
		  +  4  +  5  +   6  +
		  +-----+-----+------+
		  +     +     +      +
		  +  7  +  8  +   9  +
		  +-----+-----+------+ 

		   Type the number in appropriate boxes when prompted

4.) A player wins when their symbol is in three consecutive boxes wether vertical or horizontal or diagonally present.
5.) Enjoy the game !!!
		"""

		if raw_input() == "":
			pass

def end_credit():
    msg_end = "Backbencher's Games"
    end = [[" " for i in range(47)]for i in range(14)]
    for i in range(len(msg_end)):
        end[10][i+11] = msg_end[i]

    for row in end:
        print " ".join(map(str,row))
        print ""
    time.sleep(2)
    os.system('clear')
    sys.exit()


def menu():
	os.system('clear')
	menu = """

			WELCOME TO TIC-TAC-TOE


		1.) Press 1 to play the game with computer.
		2.) Press 2 to play the game with another player.
		3.) Press 3 to Exit.
			"""
	print menu

	temp = input()

	if temp == 1:
		return "init_one_pl"
	elif temp == 2:
		return "init_two_pl"
	elif temp == 3:
		os.system('clear')
		end_credit()

def display(board):


	for i in range(3):
		print "               +--------+--------+--------+           "
		print "               +        +        +        +           "
		print "               +",

		for j in range(3):
			if j == 2:
				print "  ",	
				print str(board[i][j]) + "   +"
				print "               +        +        +        +           "
				if i == 2:
					print "               +--------+--------+--------+           "

			else:
				print "  ",
				print str(board[i][j]),

				print "  +",



while True:

	board = [[" " for x in range(3)]for x in range(3)]

	temp = menu()

	if temp == "init_two_pl":

		Instructions("two_pl")

		print "Enter Player 1 name: "
		player1 = raw_input()
		print "Enter player 2 name: "
		player2 = raw_input()

		os.system('clear')
		display(board)

		print player1 + " Choose the symbol: 'X' or 'O'"

		pl1_symb = raw_input()

		if pl1_symb == "X":

			pl2_symb = "O"
		else:
			pl2_symb = "X"

		c = 0
		turn = 1
		flag = 0

		while True:

			if flag == 1:
				break

			if c == 9:

				print "              ----- >> DRAW << -----              "
				print "Would you like to replay?"
				if raw_input() == "yes":
					flag = 0
					c = 0
					continue
				break

			if turn == 1:

				curr_player = player1
				curr_symbol = pl1_symb
			else:

				curr_player = player2
				curr_symbol = pl2_symb

			print curr_player + " : Enter the postion from 1 to 9 : "

			pos = input()

			if pos == 0 or pos > 9:
				continue

			i, j = position.positionnum(pos)

		
			while True:

				if flag == 1:
					if raw_input():
						pass
					break
				if board[i][j] != " ":

					
					os.system('clear')
					display(board)
				
					print curr_player + " : Choose another place in grid : "

					break
				else:

					board[i][j] = curr_symbol

					os.system('clear')
					display(board)
					

					if checkConstraintfinal1.CheckConstraints(pos, board, 0, "", ""):

						print curr_player + " Wins the game !!!"

						print ""
						print "Would you like to try again yes/no?"
						if raw_input() == "yes":
							board = [[" " for x in range(3)]for x in range(3)]
							flag = 0
							os.system('clear')
							display(board)
							c = 0
							break

						else:
							flag = 1
							break

					else:
						c += 1
						if turn == 1:

							turn = 2
						else:

							turn = 1

						break

	else:

		Instructions("one_pl")
			
		print "Enter your name :"
		player = raw_input()

		os.system('clear')

		display(board)
		print player + " Choose a symbol:  'X' or 'O'"
		pl_symb = raw_input()

		while True:
			if pl_symb == 'X':
				
				comp_symb = 'O'
				break
			elif pl_symb == 'O':

				comp_symb = 'X'
				break

			else:
				print "Enter the symbol :  'X' or 'O'"
				pl_symb = raw_input()
				continue

		c = 0
		turn = 1
		flag = 0

		position_remaining = [1, 2, 3, 4, 5, 6, 7, 8, 9] ## Occupied position in board
		comp_pos = [] ## Opponent position for computer
		player_pos = []

		while True:

			if flag == 1:
				break

			if c == 9:
				print "              ----- >> DRAW << -----              "
				if raw_input() == "":
					print "would you like to replay yes/no?"
					if raw_input() == "yes":
						position_remaining = [1, 2, 3, 4, 5, 6, 7, 8, 9] ## Occupied position in board
						board = [[" " for x in range(3)]for x in range(3)]
						comp_pos = [] ## Opponent position for computer
						player_pos = []
						flag= 0
						c = 0
						continue
					else:
						flag = 1
						break


			if turn == 1:

				curr_player = player
				curr_symbol = pl_symb
			else:

				curr_player = "Comp_AI"
				curr_symbol = comp_symb

			if curr_player == "Comp_AI":

				i, j = AI.Play(board, comp_pos, player_pos, comp_symb, pl_symb, position_remaining)
				pos = position.positionnum([i, j])
			else:

				print curr_player + " : Enter the postion from 1 to 9 : "
				pos = input()

				if pos == 0 or pos > 9:

					continue
				else:

					i, j = position.positionnum(pos)

			while True:

				if flag == 1:
					break

				if board[i][j] != " ":
					
					os.system('clear')
					display(board)
				
					print curr_player + " : Choose another place in grid : "
					break
				else:

					board[i][j] = curr_symbol
					if curr_player == "Comp_AI":
						comp_pos.append(pos)
					else:
						player_pos.append(pos)
					
					position_remaining.remove(pos)

					os.system('clear')
					display(board)

					if checkConstraintfinal1.CheckConstraints(pos, board, 0, "", ""):

						print curr_player + " Wins the game !!!"

						print ""
						print "Would you like to try again yes/no?"
						if raw_input() == "yes":
							board = [[" " for x in range(3)]for x in range(3)]
							flag = 0
							position_remaining = [1, 2, 3, 4, 5, 6, 7, 8, 9] ## Occupied position in board
							board = [[" " for x in range(3)]for x in range(3)]
							comp_pos = [] ## Opponent position for computer
							player_pos = []
							os.system('clear')
							display(board)
							c = 0
							break

						else:
							flag = 1
							break

					else:
						c += 1
						if turn == 1:

							turn = 2
						else:

							turn = 1

						break

