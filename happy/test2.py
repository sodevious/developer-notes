import json

stored = json.load("data.json")

words = [ 
"adjective", 
"noun1", 
"noun2" 
] 


stored_words = {} 

for word in words: 
	answer = raw_input("Please enter a %s:" % word) 
	stored_words[word] = answer 


j = json.dumps(stored_words, indent=4)
f = open('sample.json', 'w')
print >> f, j
print stored_words
f.close()

