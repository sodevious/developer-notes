import json

filename = 'things.json'
try:
	f = open(filename, 'r')
	things = json.load(f)
except (IOError, ValueError):
	things = []

words = [ 
	"adjective", 
	"noun1", 
	"noun2" 
] 

stored_words = {} 
for word in words: 
	answer = raw_input("Please enter a %s:" % word) 
	stored_words[word] = answer 

things.append(stored_words)

f = open(filename, 'w')
json.dump(things, f, indent=4)
f.close()


