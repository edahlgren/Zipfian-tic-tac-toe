from Engine import *
from Presentation import *
import sys

"""
A module to allow the artificial intelligence and the human player to interact for a single game, or even for a sequence of games.

Author: Erin Dahlgren

Date: November 2011

"""





def translate_board(board, map):
	"""
	Translates list values to a map's values	

	Args:
		board: a 2d list of chars, where 
			chars = 'X' or 'O' or '.'
		map: a hashmap that associates each 
			(row,col) in board with a value

	Returns:
		board: a 2d list of chars with the map 
		values in place of the (row,col) values

	"""
	copy = generate_copy(board)
	empty_spaces = status(copy, '.')
	for (i,j) in empty_spaces:
		copy[i][j] = map[(i,j)]
	return copy 





def translate_move(choice, map):
	"""
	Translates a map value back to its associated key	

	Args: 
		choice: an int from 0-9, signifying which 
			board position the human wants
		map: the hashmap that originally translated 
			list values to ints 0-9

	Returns:
		(row,col) key in hashmap that corresponds to 
		the human's 0-9 choice

	"""
	map_reverse = dict((value, key) for key, value in map.items())
        move = map_reverse[int(choice.strip())]
	return move



def prompt(board):
	"""
	Displays the current tic tac toe board to the 
	human player and solicits their next move

	Args:
		board: a 2d list of chars, where 
			chars = 'X', or 'O', or '.'

	Returns:
		(row,col) board position
	"""
	spaces = {
		(0,0) : 1, (0,1) : 2, (0,2) : 3, 
		(1,0) : 4, (1,1) : 5, (1,2) : 6, 
		(2,0) : 7, (2,1) : 8, (2,2) : 9}
	board_to_display = translate_board(board, spaces)
	print_game(board_to_display)
	print " "
	print "Type the number of an open space:"
	human_choice = sys.stdin.readline()
	possibles = [str(i) for i in range(0,10)]
	if(human_choice.strip() in possibles):	
		move = translate_move(human_choice, spaces)
		return move
	else:
		prompt(board)




def update(move, mark, board):
	"""
	Args:
		move: a tuple (row,col) corresponding 
			to a position on the board
		mark: a player's mark = 'X' or 'O'
		board: a 2d list of chars, where 
			chars = 'X' or 'O' or '.'

	Returns:
		board with mark in place (row,col)
	"""
	board[move[0]][move[1]] = mark
	return board





def checkover(board):
	"""
	Checks for endgame	

	Args:
		board: a 2d list of chars, where 
			chars = 'X' or 'O' or '.'

	Returns:
		True if either there is a tie or a win
	"""
	return (checkwin(board, 'X') or checkwin(board, 'O') or checktie(board))





def human_move(board):
	"""
	Solicits human's choice, updates the game, 
	hands off choice to George (computer)

	Args:
		board: a 2d list of chars, where 
			chars = 'X' or 'O' or '.'

	Returns:
		(nothing) instead forces move_sequence 
		function to recurse
	"""	
	human = prompt(board)
	if(human in status(board, '.')):
		make_space(2)
		print "You moved: ", human[0], human[1]
		make_space(1)
		updated = update(human, 'X', board)
		move_sequence(updated, 'O')
	else: human_move(board)





def move_sequence(board, mark):
	"""
	Recurses until game is at endgame, switching 
	between human move and George's move

	Args:
		board: a 2d list of chars, where 
			chars = 'X' or 'O' or '.'
		mark: a player's mark = 'X' or 'O'

	Returns:
		board at endgame, with a message for 
		whomever has won
	"""	
	if(not(checkover(board))):
		if(mark == 'X'):
			human_move(board)
		if(mark == 'O'):
			choices = optimals(board, 'O', 'X')
			computer = choose(choices, board, 'O', 'X')
			print "George moved: ", computer[0], computer[1]
			make_space(2)
			updated = update(computer, 'O', board)
			move_sequence(updated, 'X') 
	if(checkover(board)):
		win_message = "There is no winner: You and George are at a draw!"
		if(checkwin(board, 'O')):
			win_message = "George has beaten you!"
		return (board, win_message)





def replay():
	"""
	Provides option to replay at end of each game

	Args:
		(none)
	
	Returns:
		'done' string if no replay; otherwise 
		calls game again
	"""
	print "type 'Y' (no quotes) or 'N' (no quotes)"
	reset = sys.stdin.readline()
	reset = reset.strip()
	if(reset == 'Y' or reset == 'y'):
		game()
	elif(reset == 'N' or reset == 'n'):
                return 'done'
	else:
		print "I think you mistyped:"
		replay()





def game():
	"""
	Starts a new game with empty board, runs through 
	move sequence, prints endgame and allows replay

	Args:
		(none)

	Returns:		
		(nothing) instead prints endgame and calls 
		sister function replay
	"""
	board = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
	endgame = move_sequence(board, 'X')
	print_game(endgame[0])
	print "End of game!", endgame[1]
	print " "
	#Make another function for this
	print "Would you like to play again?"
	replay()





def return_options():
	"""
	Allows human to return to main options	

	Args:
		(none)
	
	Returns:
		(nothing) instead calls main menu or 
		itself if user mistypes
	"""
	print "type 'back' (no quotes) to return to main options"
	back = sys.stdin.readline()
	if back == 'back\n':
		choose_action()
	else:
		return_options()





def choose_action():
	"""
	Main menu: learn about Zipf, learn about Rules, 
	play game, or exit

	Args:
		(none)

	Returns:
		(nothing) instead calls function that 
		corresponds to menu option; 
		otherwise human mistyped and calls itself
	"""
	make_space(2)
	print "type 'play' (no quotes) if you would like to play straight away,"
	print "type 'Zipf' (no quotes) to learn more about your opponent"
	print "type 'rules' (no quotes) to learn about the game rules"
	print "type 'exit' (no quotes) to exit game"
	PlayorZipf = sys.stdin.readline()
	PlayorZipf = PlayorZipf.strip()
	if(PlayorZipf == 'Zipf'):
	        make_space(6)
		about_zipf()
		make_space(1)
	        return_options()
	elif(PlayorZipf == 'rules'):
		make_space(6)
	        about_rules()
		make_space(1)
		return_options()
	elif(PlayorZipf == 'play'):
		make_space(6)
		about_game()
		make_space(1)
	        game()
		make_space(1)
		return_options()
	elif(PlayorZipf == 'exit'):
		make_space(6)
	        print "       Have an engaging day!"
	        print "       Make sure to look up George Kingsley Zipf."
	else:
		make_space(4)
	        print "I think you mistyped.  Please choose:"
	        make_space(1)
	        choose_action()










