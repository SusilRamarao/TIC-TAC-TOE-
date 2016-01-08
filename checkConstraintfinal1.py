def CheckConstraints(position, board, predict, temp_symbol, direction):
	temp_strike = dict()
	
	def down(coord, temp):
		temp_strike = []
		if temp == "X":
			opp_temp = "O"
		else:
			opp_temp = "X"

		i, j = coord[0], coord[1]
		count = 0
		emp_index = []

		for x in range(3):
			if predict == 0 and board[x][j] == temp:
				true = 1
				continue

			elif predict == 1 and board[x][j] == temp:
				count += 1
				continue
				
			elif predict == 1 and board[x][j] == " ":
				continue

			elif predict == 1 and board[x][j] == opp_temp:
				count = 0
				break

			elif predict == 3 and board[x][j] == temp:
				continue

			elif predict == 3 and board[x][j] != temp:
				return [x, j]

			else:
				true = 0
				break


		if predict == 1:
			return count
		

		if predict == 0 and true == 1:
			return True
		else:
			return False

	def right(coord, temp):

		if temp == "X":
			opp_temp = "O"
		else:
			opp_temp = "X"


		i, j = coord[0], coord[1]
		count = 0

		for x in range(3):
			if predict == 0 and board[i][x] == temp:
				true = 1
				continue

			elif predict == 1 and board[i][x] == temp:
				count += 1
				continue
				
			elif predict == 1 and board[i][x] == " ":
				continue

			elif predict == 1 and board[i][x] == opp_temp:
				count = 0
				break

			elif predict == 3 and board[i][x] == temp:
				continue
			elif predict == 3 and board[i][x] != temp:
				return [i, x]
			else:
				true = 0
				break

		if predict == 1:
			return count

		if predict == 0 and true == 1:
			return True
		else:
			return False

	def diagonal(coord, temp):

		i, j = coord[0], coord[1]
		count = 0
		emp_index = []

		if temp == "X":
			opp_temp = "O"
		else:
			opp_temp = "X"

		if j == 0:

			for x in range(3):
				if predict == 0 and board[x][j] == temp:
					true = 1
					j += 1
					continue

				elif predict == 1 and board[x][j] == temp:
					count += 1
					j += 1
					continue

				elif predict == 1 and board[x][j] == " ":
					j += 1
					continue

				elif predict == 1 and board[x][j] == opp_temp:
					count = 0
					break
				elif predict == 3 and board[x][j] == temp:
					j += 1
					continue
				elif predict == 3 and board[x][j] != temp:
					return [x, j]
				elif predict == 0:
					true = 0
					break


		else:
			

			for x in range(3):
				if predict == 0 and board[x][j] == temp:
					true = 1
					j -= 1
					continue

				elif predict == 1 and board[x][j] == temp:
					count += 1
					j -= 1
					continue

				elif predict == 1 and board[x][j] == " ":
					j -= 1
					continue

				elif predict == 1 and board[x][j] != temp:
					count = 0
					break
				elif predict == 3 and board[x][j] == temp:
					j -= 1
					continue
				elif predict == 3and board[x][j] != temp:
					return [x, j]
				else:
					true = 0
					break
		
		if predict == 1:
			return count
		
		if predict == 0 and true == 1:
			return True
		else:
			return False


	if position == 1:

		temp_strike["down"] = None
		temp_strike["right"] = None
		temp_strike["diagonal"] = None

		coord = [0, 0]
		
		if predict == 1 or predict == 3:
			symbol = temp_symbol
		else:

			symbol = board[0][0]
		
		if predict == 1 or predict == 0 or (predict == 3 and direction == "down"):
			rec = down(coord, symbol)
			if predict == 1:
				temp_strike["down"] = rec
			elif predict == 3:
				return rec
			elif predict == 0 and rec == True:
				return True


		if predict == 1 or predict == 0 or (predict == 3 and direction == "right"):
			rec = right(coord, symbol)
			if predict == 1:
				temp_strike["right"] = rec
			elif predict == 3:
				return rec
			elif predict == 0 and rec == True:
				return True

		if predict == 1 or predict == 0 or (predict == 3 and direction == "diagonal"):
			rec = diagonal(coord, symbol)
			if predict == 1:
				temp_strike["diagonal"] = rec
				return temp_strike
			elif predict == 3:
				return rec

			elif predict == 0 and rec == True:
				return True
			else:
				return False


	elif position == 2:
		temp_strike["right"] = None
		temp_strike["down"] = None
		coord = [0, 1]

		if predict == 1 or predict == 3:
			symbol = temp_symbol
		else:
			symbol = board[0][1]

		if predict == 0 or predict == 1 or (predict == 3 and direction == "down"):
			rec = down(coord, symbol)
			if predict == 1:
				temp_strike["down"] = rec
			elif predict == 3:
				return rec
			elif predict == 0 and rec == True:
				return True


		coord = [0, 0]

		if predict == 1 or predict == 3:
			symbol = temp_symbol

		if predict == 0 or predict == 1 or (predict == 3 and direction == "right"):
			rec = right(coord, symbol)
			if predict == 1:
				temp_strike["right"] = rec
				return temp_strike
			elif predict == 3:
				return rec
			elif predict == 0 and rec == True:
				return True
			else:
				return False

	elif position == 3:

		temp_strike["right"] = None
		temp_strike["down"] = None
		temp_strike["diagonal"] = None

		coord = [0, 2]
		symbol = board[0][2]

		if predict == 1 or predict == 3:
			symbol = temp_symbol
		else:
			symbol = board[0][2]

		if predict == 0 or predict == 1 or (predict == 3 and direction == "down"):
			rec = down(coord, symbol)
			if predict == 1:
				temp_strike["down"] = rec
			elif predict == 3:
				return rec
			elif predict == 0 and rec == True:
				return True

		if predict == 0 or predict == 1 or (predict == 3 and direction == "diagonal"):
			rec = diagonal(coord, symbol)
			if predict == 1:
				temp_strike["diagonal"] = rec
			elif predict == 3:
				return rec
			elif predict == 0 and rec == True:
				return True

		coord = [0, 0]

		if predict == 0 or predict == 1 or (predict == 3 and direction == "right"):
			rec = right(coord, symbol)
			if predict == 1:
				temp_strike["right"] = rec
				return temp_strike
			elif predict == 3:
				return rec
			elif predict == 0 and rec == True:
				return True
			else:
				return False


	elif position == 4:

		temp_strike["right"] = None
		temp_strike["down"] = None
		coord = [1, 0]

		if predict == 1 or predict == 3:
			symbol = temp_symbol
		else:
			symbol = board[1][0]

		if predict == 0 or predict == 1 or (predict == 3 and direction == "right"):
			rec = right(coord, symbol)
			if predict == 1:
				temp_strike["right"] = rec
			elif predict == 3:
				return rec
			elif predict == 0 and rec == True:
				return True

		coord = [0, 0]

		if predict == 0 or predict == 1 or (predict == 3 and direction == "down"):
			rec = down(coord, symbol)
			if predict == 1:
				temp_strike["down"] = rec
				return temp_strike
			elif predict == 3:
				return rec
			elif predict == 0 and rec == True:
				return True
			else:
				return False



	elif position == 5:

		temp_strike["down"] = None
		temp_strike["right"] = None
		temp_strike["diagonalr"] = None
		temp_strike["diagonall"] = None

		coord = [0, 1]

		if predict == 1 or predict == 3:
			symbol = temp_symbol
		else:
			symbol = board[1][1]

		if predict == 0 or predict == 1 or (predict == 3 and direction == "down"):
			rec = down(coord, symbol)
			if predict == 1:
				temp_strike["down"] = rec
			elif predict == 3:
				return rec
			elif predict == 0 and rec == True:
				return True

		coord = [0, 0]

		if predict == 0 or predict == 1 or (predict == 3 and direction == "diagonalr"):
			rec = diagonal(coord, symbol)
			if predict == 1:
				temp_strike["diagonalr"] = rec
			elif predict == 3:
				return rec
			elif predict == 0 and rec == True:
				return True


		coord = [0, 2]

		if predict == 0 or predict == 1 or (predict == 3 and direction == "diagonall"):
			rec = diagonal(coord, symbol)
			if predict == 1:
				temp_strike["diagonall"] = rec
			elif predict == 3:
				return rec
			elif predict == 0 and rec == True:
				return True


		coord = [1, 0]

		if predict == 0 or predict == 1 or (predict == 3 and direction == "right"):
			rec = right(coord, symbol)
			if predict == 1:
				temp_strike["right"] = rec
				return temp_strike

			elif predict == 3:
				return rec
			elif predict == 0 and rec == True:
				return True
			else:
				return False


	elif position == 6:

		temp_strike["down"] = None
		temp_strike["right"] = None
		coord = [0, 2]

		if predict == 1 or predict == 3:
			symbol = temp_symbol
		else:
			symbol = board[1][2]

		if predict == 0 or predict == 1 or (predict == 3 and direction == "down"):
			rec = down(coord, symbol)
			if predict == 1:
				temp_strike["down"] = rec
			elif predict == 3:
				return rec
			elif predict == 0 and rec == True:
				return True


		coord = [1, 0]

		if predict == 0 or predict == 1 or (predict == 3 and direction == "right"):
			rec = right(coord, symbol)
			if predict == 1:
				temp_strike["right"] = rec
				return temp_strike

			elif predict == 3:
				return rec
			elif predict == 0 and rec == True:
				return True
			else:
				return False		

	elif position == 7:
		temp_strike["right"] = None
		temp_strike["down"] = None
		temp_strike["diagonal"] = None

		coord = [2, 0]

		if predict == 1 or predict == 3:
			symbol = temp_symbol
		else:
			symbol = board[2][0]

		if predict == 0 or predict == 1 or (predict == 3 and direction == "right"):
			rec = right(coord, symbol)
			if predict == 1:
				temp_strike["right"] = rec
			elif predict == 3:
				return rec
			elif predict == 0 and rec == True:
				return True


		coord = [0, 0]


		if predict == 0 or predict == 1 or (predict == 3 and direction == "down"):
			rec = down(coord, symbol)
			if predict == 1:
				temp_strike["down"] = rec
			elif predict == 3:
				return rec
			elif predict == 0 and rec == True:
				return True


		coord = [0, 2]
		if predict == 0 or predict == 1 or (predict == 3 and direction == "diagonal"):
			rec = diagonal(coord, symbol)
			if predict == 1:
				temp_strike["diagonal"] = rec
				return temp_strike
			elif predict == 3:
				return rec
			elif predict == 0 and rec == True:
				return True
			else:
				return False


	elif position == 8:

		temp_strike["down"] = None
		temp_strike["right"] = None

		coord = [2, 0]

		if predict == 1 or predict == 3:
			symbol = temp_symbol
		else:
			symbol = board[2][1]

		if predict == 0 or predict == 1 or (predict == 3 and direction == "right"):
			rec = right(coord, symbol)
			if predict == 1:
				temp_strike["right"] = rec

			elif predict == 3:
				return rec
			elif predict == 0 and rec == True:
				return True

		coord = [0, 1]
		if predict == 0 or predict == 1 or (predict == 3 and direction == "down"):
			rec = down(coord, symbol)
			if predict == 1:
				temp_strike["down"] = rec
				return temp_strike
			elif predict == 3:
				return rec
			elif predict == 0 and rec == True:
				return True
			else:
				return False


	elif position == 9:

		temp_strike["down"] = None
		temp_strike["right"] = None
		temp_strike["diagonal"] = None

		coord = [0, 0]

		if predict == 1 or predict == 3:
			symbol = temp_symbol
		else:
			symbol = board[2][2]

		if predict == 0 or predict == 1 or (predict == 3 and direction == "diagonal"):
			rec = diagonal(coord, symbol)
			if predict == 1:
				temp_strike["diagonal"] = rec
			elif predict == 3:
				return rec
			elif predict == 0 and rec == True:
				return True

		coord = [0, 2]
		if predict == 0 or predict == 1 or (predict == 3 and direction == "down"):
			rec = down(coord, symbol)
			if predict == 1 :
				temp_strike["down"] = rec
			elif predict == 3:
				return rec
			elif predict == 0 and rec == True:
				return True

		coord = [2, 0]
		if predict == 0 or predict == 1 or (predict == 3 and direction == "right"):
			rec = right(coord, symbol)
			if predict == 1:
				temp_strike["right"] = rec
				return temp_strike
			elif predict == 3:
				return rec
			elif predict == 0 and rec == True:
				return True
			else:
				return False
