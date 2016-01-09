from checkConstraintfinal1 import CheckConstraints
import position
import changeboard


def winstrike(board, position, temp_symbol):
	temp_winstrike = dict()

	for i in position:

		temp_winstrike[i] = CheckConstraints(i, board, 1, temp_symbol, "")

	return temp_winstrike

def Play(board, Comp_position, Opp_position, Comp_symbol, player_symbol, pos_remain):
	comp_winstrike = dict()
	player_winstrike = dict()

	comp_winstrike = winstrike(board, Comp_position, Comp_symbol)

	player_winstrike = winstrike(board, Opp_position, player_symbol)

	for i in comp_winstrike:
		keys = comp_winstrike[i].keys()
		values = comp_winstrike[i].values()
		
		if 2 in values:
			ind = values.index(2)
			key = keys[ind]
			return CheckConstraints(i, board, 3, Comp_symbol, key)

	for i in player_winstrike:

		keys = player_winstrike[i].keys()
		values = player_winstrike[i].values()

		if 2 in values:

			ind = values.index(2)
			key = keys[ind]
			return CheckConstraints(i, board, 3, player_symbol, key)


	corner = [1, 3, 7, 9]

	for i in corner:
		if (i in Comp_position) or (i in Opp_position):
			continue
		else:
			return position.positionnum(i)
			
	return position.positionnum(random.choise(pos_remain))

	



##win_Strike counts the number of places needed to win the game for a player

	
