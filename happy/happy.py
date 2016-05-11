# import json


# stored_words = [] 


# answer = raw_input("What makes you happy today?") 
# stored_words.append(answer) 



# j = json.dumps(answer, indent=4)




# print(stored_words)

#import okcupid
import math
 
def date():
	print ' '
	print 'Welcome to my program.'
	print 'Please answer all questions with an integer.'
	print 'On the scale of 1-10.'
	print 'NO CHEATING'
	print ' '
 
	phone_number = "###-###-####"
 
	funniness = int(raw_input('On a scale of 1-10, how funny are you? '))
	adventurous = int(raw_input('On a scale of 1-10, how adventurous do you consider yourself? '))
	fufillment = int(raw_input('On a scale of 1-10, how often do you go after what you want? '))
	nerdiness = int(raw_input('On a scale of 1-10, how nerdy are you?!'))
	happiness = int(raw_input('Rate your happiness on a scale of 1-10.'))
 
	subtotal = ((adventurous + funniness + fufillment / 1.15) + (nerdiness + happiness / 0.65)) / 5
	 
	print 'Your score: ', subtotal
 
	if subtotal >= 7.5:
		print 'Congratulations! Call me.', phone_number
	else:
		print 'Bummer. You did not pass. Try again next time?'
 
date()