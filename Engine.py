from Presentation import george
import itertools
import sys

"""
A module to drive the decision making of an artificial intelligence in The George Kingsley Zipf Tic Tac Toe game.

Author: Erin Dahlgren

Date: November 2011

"""





def status(board, who):
	"""
	Fetches positions on a tic tac toe board for a given mark

	Args:
		board: a 2d list of chars, where 
			chars = 'X', 'O' or '.'
		who: 'X', 'O', or '.'

	Returns:
		list of indices (rows, cols) where char 
		value occurs
	"""
	who_marks = []
	for i in range(0, len(board)):
		for j in range(0, len(board)):
			if(board[i][j] == who):
				who_marks.append((i,j))			
	return who_marks





def checkwin(board, who):
	"""
	Maps player marks to values. A combination of 3 values 
	signifies a win if and only if their sum = 15	
	
	Args:
		board: a 2d list of chars, where 
			chars = 'X' or 'O' or '.'
		who: 'X' or 'O'

	Returns:
		True only if 'who' has won the tic tac toe game
	"""
	listwho = status(board, who)
	winmap = {
			(0,0) : 8, (0,1) : 3, (0,2) : 4, 
			(1,0) : 1, (1,1) : 5, (1,2) : 9, 
			(2,0) : 6, (2,1) : 7, (2,2) : 2}
	for i in range(0, len(listwho)):
		listwho[i] = winmap[listwho[i]]
	if len(listwho) > 2:
		for subset in itertools.combinations(listwho, 3):
			summed = sum(subset)
			if(summed == 15):
				return True
	else: return False





def checktie(board):
	"""	
	Args:
		board: a 2d list of chars, where 
			chars = 'X' or 'O' or '.'

	Returns:
		True only if both 'X' and 'O' do not 
		return True in checkwin and only if 
		there are no empty space marks '.'
	"""
	full = (status(board, '.') == [])
	if(full and (checkwin(board, 'X') == checkwin(board, 'O'))):
		return True
	else: return False





def generate_copy(board):
	"""
	Copies the values of one board to another that is 
	saved in a different location in memory

	Args:
		board: a 2d list of chars, where 
			chars = 'X' or 'O' or '.'

	Returns:
		board: a 2d list of chars, where 
		chars = 'X' or 'O' or '.'
	"""
	copy = [['.' for y in range(0, len(board))] for x in range(0, len(board))]
        for i in range(0, len(board)):
                for j in range(0, len(board)):
                        copy[i][j] = board[i][j]
	return copy





def xwin(board, p1, p2):
	"""
	Args:
		board: a 2d list of chars, where 
			chars = 'X' or 'O' or '.'
		p1: player 1's mark, either 'X' or 'O'
		p2: player 2's mark, either 'O' or 'X'

	Returns:
		True only if p2 can win at some empty 
		space on the current board
	"""
	children = status(board, '.')
	if(children != []):
		for (i,j) in children:
			board[i][j] = p2
			if(checkwin(board, p2)):
				return True
			board[i][j] = '.'
	return False





def optimals(board, p1, p2):
	"""
	Filters the empty spaces on the board for 
	optimal position(s)

	Args:
		board: a 2d list of chars, where 
			chars = 'X' or 'O' or '.'
		p1: player 1's mark, either 'X' or 'O'
		p2: player 2's mark, either 'O' or 'X'

	Returns:
		A list of (row,col) indices on the board 
		that ensure that p1 will either immediately 
		win or at least not die
	"""
	optimal = []
	DecisionNodes = status(board, '.')
	for x in DecisionNodes:
		copy = generate_copy(board)
		(i,j) = x
		copy[i][j] = p1
		if(checkwin(copy, p1)):
			return [x]
		if(not(xwin(copy, p1, p2))):
			optimal.append(x)
		copy[i][j] = '.'
	if(optimal == []):
		optimal.append(DecisionNodes[0])
	return optimal





def choices_to_boards(opchoices, board, p1):
	"""
	Places each optimal choice for player 1 on a 
	different copy of the original board	
		
	Args:
		opchoices: a list of optimal choices 
			returned by optimals
		board: a 2d list of chars, where 
			chars = 'X' or 'O' or '.'
		p1: player 1's mark, either 'X' or 'O'

	Returns:
		A list of boards: a list of 2d lists of chars
	"""
	boards = []
        for (i,j) in opchoices:
                copy = generate_copy(board)
                copy[i][j] = p1
                boards.append(copy)
        return boards





Owins = 0
Xwins = 0
ties = 0
"""
global variables to protect the win, loss, and tie 
cumulative counting done by the recursion in recurse_tree

"""





def recurse_tree(board, p1, p2):
	"""
	Recurses through all nodes in the game tree under 
	parent node board (args) and tallies up all endgame 
	results at terminal nodes

	Args:
		board: a 2d list of chars, where 
			chars = 'X' or 'O' or '.'; also 
			a meaningful node in the game tree
		p1: player 1's mark, either 'X' or 'O'
		p2: player 2's mark, either 'O' or 'X'

	Returns:
		A 3 element list: total O wins, X wins, and 
		tie for all endgames under board node in the 
		full game tree
	"""	
	global Owins
	global Xwins
	global ties
	children = status(board, '.')
	if(children == []):
		return 'no children'
	else:
		for child in children:
			(i,j) = child
			board[i][j] = p2
			if(checkwin(board, 'X')):
				Xwins += 1
			elif(checkwin(board, 'O')):
				Owins += 1
			elif(checktie(board)):
				ties +=	1
			else:
				recurse_tree(board, p2, p1)
			board[i][j] = '.'
	return [Owins, Xwins, ties]





def checkdiag(board, opponent):
	"""
	Checks for potential double fork situation.  
	Read more about this in Engine.pdf

	Args:
		board: 2d list of chars, where 
			chars = 'X' or 'O' or '.'
		opponent: mark opposite to the player 
			currently choosing a move

	Returns:
		True only if board is set up for a potential 	
		double fork: in an 'every-other-mark' diagonal 
		with only 3 marks on the board
	"""	
	addmap = {
			(0,0) : 4, (0,1) : 0, (0,2) : 2, 
			(1,0) : 0, (1,1) : 0, (1,2) : 0, 
			(2,0) : 6, (2,1) : 0, (2,2) : 4}
	sum = 0
	opp = status(board, opponent)
	c = (len(opp) == 2)
	for i in opp:
		sum = sum + addmap[i]
	if c and (sum == 8):
		return True
	else: return False





def rotate(indices):
	"""
	Rotates the board 45 degrees counterclockwise and 
	project downwards
	
	Args:
		indices: a list of (row,col) tuples of optimal 
			empty spaces on the board

	Returns:
		indices: a list of (row,col) tuples of optimal 
		emtpy spaces on the board, but rotated in place
	"""	
	degree45 = {
			(0,0) : (1,0), (0,1) : (0,0), (0,2) : (0,1), 
			(1,0) : (2,0), (1,1) : (1,1), (1,2) : (0,2), 
			(2,0) : (2,1), (2,1) : (2,2), (2,2) : (1,2)}
	for i in range(0, len(indices)):
		indices[i] = degree45[indices[i]]
	return indices





def get_stats(indices, originalboard, p1, p2):
	"""
	Collects and organizes the win, loss, and tie counts 
	returned by the recursion 

	Args:
		indices: a list of (row,col) tuples of optimal 
			empty spaces on the board 
		originalboard: the 2d list of chars on which 
			the current player needs to move
		p1: player 1's mark, either 'X' or 'O'
		p2: player 2's mark, either 'O' or 'X'

	Returns:
		A 2d list of counts, grouping wins together, 
		losses together, and ties together

	"""
	global Owins
        global Xwins
        global ties
        stats = [[], [], []]
        boards = choices_to_boards(indices, originalboard, p1)
	for i in range(0, len(boards)):
                Owins = 0
                Xwins = 0
                ties = 0
                wins = recurse_tree(boards[i], p1, p2)
                if i  == (len(boards)-1):
                        george(9)
                stats[0].append(wins[0])
                stats[2].append(wins[2])
                if(wins[1] != 0):
                        stats[1].append(wins[1])
                else:
                        stats[1].append(1)
        return stats





def compute_stats(stats, indices, originalboard, opponent):
	"""
	Args:
		stats: the win, loss, and tie counts returned by 				stats in 2d list
		indices: maps to stats[i], where i = 0, 1, or 2
		originalboard: the 2d list of chars on which 
			the current player needs to move
		opponent: opponent: mark opposite to the player 
			currently choosing a move

	Returns:
		(row,col) position where losses/wins+ties+losses 
		is minimized		

	"""
	if(checkdiag(originalboard, opponent) == True):
		indices = rotate(indices)
	for j in range(0, len(stats[1])):
		stats[2][j] = stats[1][j]/float(stats[0][j] + stats[1][j] + stats[2][j])
	return indices[stats[2].index(min(stats[2]))]





def choose(indices, originalboard, p1, p2):
	"""
	Chooses the best move	

	Args:
		indices: a list of (row,col) tuples of optimal 
			empty spaces on the board
		originalboard: the 2d list of chars on which 
			the current player needs to move
		p1: player 1's mark, either 'X' or 'O'
		p2: player 2's mark, either 'O' or 'X'

	Returns:
		the only indice if indices (args) has only one 
		element, the best indice if indices (args) has 
		more than one element

	"""
	if(len(indices) == 1):
                george(9)
                return indices[0]
        elif(len(indices) > 1):
                george(8)
                stats = get_stats(indices, originalboard, p1, p2)
                return compute_stats(stats, indices, originalboard, p2)

 













