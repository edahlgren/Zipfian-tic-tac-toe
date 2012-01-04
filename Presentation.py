

"""
A module to display informational graphics or supplementary text to the human player

Author: Erin Dahlgren

Date: November 2011

"""





def make_space(num_spaces):
	"""
	Recursively generates a certain number of filler 
	blank lines, to break up text output

	Args:
		num_spaces: int blank lines desired
	"""	
	if num_spaces > 0:
		print " "
		make_space(num_spaces - 1)





def about_zipf():
	"""
	Background text about George
	"""
	print "George Kingsley Zipf, your opponent, is a" 	
	print "philologist and linguist. He mainly enjoys studying" 
	print "statistical distributions of language."
	make_space(2)
	print "When he is not hand-tallying word frequencies"
	print "from English and Chinese, he spends his free time"
	print "shopping at Sears, Roebuck, and Co."
	print "(and subsequently publishes papers on this hobby.)"  
	make_space(2)	
	print "He is a jolly fellow, but a Tic Tac Toe master."
	print "Stay on top of your toes!"
	make_space(2)
	print "View George's picture and a short history of his"
	print "ingenuity in the About_Zipf folder in this package"
	make_space(2)



def about_rules():
	"""
	Background text about the rules of tic tac toe
	"""
	print "The rules of Tic Tac Toe are straightforward"
	make_space(1)
	print "First you are assigned an 'X' or an 'O' as your mark."
	make_space(1)
	print "You are then presented with a 3x3, 9 space board."
	print "On your turn, you are only allowed to make one mark"
	print "on this 9 space board, and not where you or your"
	print "opponent has already marked."
	print "Your objective is to make your mark 3 times in either:"
	make_space(1)
	print "    A row (horizontal)"
	print "    A column (vertical)"
	print "    A diagonal"
	make_space(1)
	print "Once you have achieved this objective, you have won."
	make_space(2)




def about_game():
	"""
	Advantage of human message, displayed before first game
	"""
	print "Your mark is X and George Kingsley Zipf is O"
	print "You have the advantage of starting first, "
	print "because you will have 5 moves while George will have 4"





def george(i):
	"""
	'George thinking' messages, to make the artificial 
	intelligence jive with human interaction
	More 'thoughts' are available here than are actually used
	in the current implementation
	"""
	george_thinking = ["mmm", "A lot of possibilities: I should compute some statistics on this",  "Let's see", "mmm", "These statistics are actually pretty interesting", "mmm", "mmm",  "Okay, I think I've got it:", "Hmm, nice move.", "Here's mine:" ]
	print "George: ", george_thinking[i]
	make_space(1)





def print_game(board):
	"""
	Formats and prints game board
	
	Args:
		board: a 2d list of chars, 3 x 3 required
	"""
	edge = "+---+---+---+"
	print edge
	for i in xrange(0, 3):
		vals = "|"
		for f in xrange(0, 3):
			mark = board[i][f]
			vals = vals + " " + str(mark) + " " + "|"
		print vals
	print edge


























