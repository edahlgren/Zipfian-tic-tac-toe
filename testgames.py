from Engine import *
from Interact import *
from Presentation import *
import random


"""
A module for testing the completeness of The George Kingsley Zipf AI Engine.  See main() at bottom to run.

Author: Erin Dahlgren

Date: November 2011

"""




t = 0
Ow = 0
Xw = 0
"""
global variables to preserve cumulative O wins, X wins, and ties, 
when recursing over games 

"""





def move_sequence_itself(board, p1, p2):
	"""
	Performs a recursive move sequence for player 1 and
	player 2 when both are using George as an Engine.
	Increments global variable t in the case of tie,
	Ow in the case that player 'O' wins, and Xw in 
	the case that player 'X' wins

	Args:
		board: a 2d list of chars, where
			chars = 'X' or 'O' or '.'
		p1: player 1's mark = 'X' or 'O'
		p2: player 2's mark = 'O' or 'X'
	Returns:
		board at endgame, which can be printed if
		desired; also a win message.
	"""
	global t
	global Ow
	global Xw
	if(not(checkover(board))):
		choices = optimals(board, p1, p2)
		computer = choose(choices, board, p1, p2)
		print "player: ", p1, "move: ", computer
		updated = update(computer, p1, board)
		move_sequence_itself(updated, p2, p1)
	elif(checkover(board)):
		win_message = 'tie'
		if(checkwin(board, 'O')):
			win_message = 'O win'
			Ow += 1
		elif(checkwin(board, 'X')):
			win_message = 'X win'
			Xw += 1
		elif(checktie(board)):
			t += 1
		return board





def gen_random(board):
	"""
	Generates a random choice of a move from a set of
	empty positions on a given board

	Args:
		board: a 2d list of chars, where 
			chars = 'X' or 'O' or '.'
	
	Returns:
		(row,col) tuple corresponding to move position
	"""
	choices = status(board, '.')
	select = random.sample(choices, 1)
	return select[0]





def move_sequence_random(board, p1, p2):
	"""
	Performs a recursive move sequence for George and a 
	random player

	Args:
		board: a 2d list of chars, where
			chars = 'X' or 'O' or '.'
		p1: player 1's mark = 'X' or 'O'
		p2: player 2's mark = 'O' or 'X'
	Returns:
		board at endgame, which can be printed if
		desired; also a win message.		
	"""
	global t
	global Ow
	global Xw
	if(not(checkover(board))):
		if(p1 == 'O'):
			choices = optimals(board, p1, p2)
			computer = choose(choices, board, p1, p2)
			updated = update(computer, p1, board)
			move_sequence_random(updated, p2, p1)
		if(p1 == 'X'):
			anywhere = gen_random(board)
			updated = update(anywhere, p1, board)
			move_sequence_random(updated, p2, p1)
	elif(checkover(board)):
		win_message = 'tie'
                if(checkwin(board, 'O')):
                        win_message = 'O win'
                        Ow += 1
                elif(checkwin(board, 'X')):
                        win_message = 'X win'
                        Xw += 1
                elif(checktie(board)):
                        t += 1
                return (board, win_message)






results = []
"""
global variable to preserve a growing list of results, outside of recursive game playing

"""





def recurse_game(num_times, starter):
	"""
	Recurses through a number of games starting at 
	a fixed player 1 first move 	

	Args:
		num_times: int times to replay game
		starter: (row,col) fixed position for 
			player 1, move 1

	Returns:
		'done' string if exhausted num_times;
		else, keep recursing
	"""
	global t
	global Ow
	global Xw
	p1 = 'O'
	p2 = 'X'
	board = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
	(i,j) = starter
	board[i][j] = p2
	move_sequence_itself(board, p1, p2)
	print "game count: ", num_times
	num_times -= 1

	if num_times == -1:
		print "Total O wins: ", Ow
		print "Total X wins: ", Xw
		print "Total ties: ", t
		results = [t, Ow, Xw]
		return 'done'
	else:
		recurse_game(num_times, starter)





def play_once(p1, p2):
	"""
	George plays a random player, who starts first, ony once

	Args:
		p1 = the random player = 'X'
		p2 = George = 'O' (goes second still)

	Returns:
		cumulative ties, O wins, X wins and if possible,
		ties/O wins; if O wins = 0, ties/Owins = 0
	"""
	global t
	global Ow
	global Xw
	board = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
        (i,j) = gen_random(board)
        board[i][j] = p2
        move_sequence_random(board, p1, p2)
	if(Ow != 0):
		return [t, Ow, Xw, t/float(Ow)]
	else:
		return [t, Ow, Xw, 0]





def main():
	"""
	IMPORTANT NOTE
	navigate to Engine.py
	in function choose(indices, originalboard, p1, p2), 
	comment out lines containing 
	george(8) and george(9), or else 
	you will get unwanted text in your outputs
	"""
	global t
	global Ow
	global Xw
	p1 = 'O'
	p2 = 'X'

	"""
	Run a test of George against George where 'X's first move 
	is determined.  

	Choice (1,1) represents George's 
	optimal, desired first move, so this starter move and 
	game represents George against George proper.

	Uncomment code below, and comment-out all other tests
	"""
	#test = [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]
	#for starter in test:
	#	print "This is the starter move: ", starter
	#	recurse_game(0, starter)

	"""
	Run a test through x (saved here, x = 100) games of the 
	ties, O wins, and X wins
	Uncomment code below, and comment-out all other tests
	"""
	#iterations = 100
	#for i in range(0, iterations):
	#	x = play_once(p1, p2)
	#	print x[0],",", x[1],",", x[2],",", x[3]


if __name__ == "__main__":
	main()




"""
TIP
python testgames.py > file

to save results
"""























