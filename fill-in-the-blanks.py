# IPND Stage 2 Final Project

paragraph1 = '''A common first thing to do in a language is display 'Hello ___1___!' In ___2___ this is
particularly easy; all you have to do is type in: ___3___ "Hello ___1___!" Of course, that isn't a very
useful thing to do. However, it is an example of how to output to the user using the ___3___ command, and
produces a program which does something, so it is useful in that capacity.

It may seem a bit odd to do something in a Turing complete language that can be done even more easily with
an ___4___ file in a browser,but it's a step in learning ___2___ syntax, and that's really its purpose. '''

paragraph2 ='''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

paragraph3 = '''When you create a ___1___, certain ___2___s are automatically generated for you if you don't
make them manually. These contain multiple underscores before and after the word defining them. When you 
write a class, you almost always include at least the ___3___ ___2___, defining variables for when ___4___s
of the ___1___ get made. Additionally, you generally want to create a ___5___ ___2___, which will allow a 
string representation of the method to be viewed by other developers.'''


def check_answer(blank_num, difficulty):
	#This function takes the question number and difficulty level as input, outputs the answer of that question.

	if difficulty == 1:
		if blank_num == 1:
			return 'world'
		if blank_num == 2:
			return 'python'
		if blank_num == 3:
			return 'print'
		if blank_num == 4:
			return 'html'
	if difficulty == 2:
		if blank_num == 1:
			return 'function'
		if blank_num == 2:
			return 'arguments'
		if blank_num == 3:
			return 'None'
		if blank_num == 4:
			return 'list'
	if difficulty == 3:
		if blank_num == 1:
			return 'class'
		if blank_num == 2:
			return 'method'
		if blank_num == 3:
			return '__init__'
		if blank_num == 4:
			return 'instance'
		if blank_num == 5:
			return '__repr__'
		



def ask_question(paragraph, blank_num, guesses, difficulty):
	#This function takes the paragraph, question number, guesses left and difficulty level as input, outputs whether that question is answered correctly or not.

	if guesses == 0:		
		return False

	answer = check_answer(blank_num, difficulty)

	user_input = raw_input('\n' + paragraph + '\n\n' + 'What should be substituted in for ___' + str(blank_num) + '___? ')

	if user_input == answer:
		paragraph = paragraph.replace('___' + str(blank_num) + '___', answer)
		print 'Correct!\n\n'
		return paragraph		
	else:
		print 'False'
		print 'You have ' + str(guesses - 1) + ' guesses left.\n'
		paragraph = ask_question(paragraph, blank_num, guesses - 1, difficulty)
		if paragraph:
			return paragraph
		else:
			return False
	


def play_game(difficulty):
	#This function takes the difficulty level as input, outputs whether the user win or loses the game.

	max_question_num = 4

	if difficulty == 1:
		paragraph = paragraph1
	if difficulty == 2:
		paragraph = paragraph2
	if difficulty == 3:
		paragraph = paragraph3
		max_question_num = 5

	question_num = 1
	while question_num <= max_question_num:
		paragraph = ask_question(paragraph, question_num, 3, difficulty)
		if paragraph == False:
			print 'Game Over'
			return False
		question_num += 1

	return True



def select_mode():
	#This function starts the game and let user choose the difficulty level.

	user_input = raw_input('''
	Please select a game difficulty by typing it in!
	Possible choices include easy, medium, and hard.\n''')
	print '\n'

	if user_input == 'easy':
		if play_game(1) == True:
		 	print 'Win!'
		 	
	elif user_input == 'medium':
		if play_game(2) == True:
			print 'Win!'

	elif user_input == 'hard':
		if play_game(3) == True:
			print 'Win!'
			
	else:
		print "That's not an option"
		select_mode()



select_mode()
		

 
	
 
	













