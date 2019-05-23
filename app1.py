"""The original script"""
import json
from difflib import get_close_matches

# use get_close_matches
data = json.load(open("data.json"))

def find_word(w):
	if w in data:
		return data[w]
	elif w.title() in data:
		return data[w.title()]
	elif w.upper() in data:
		return data[w.upper()]
	elif len(get_close_matches(w, data.keys(), cutoff=0.8)) > 0:
		yn = input("Did you mean %s instead? Enter Y if yes or N if no: " % get_close_matches(w, data.keys())[0])
		if yn == "Y":
			return data[get_close_matches(w, data.keys())[0]]
		elif yn == "N":
			return("Please double check your word\nit does not exist.")
		else:
			return("Not a valid option")
	else:
		return("Please double check your word\nit does not exist.")

	
word = input("Enter word: ")
word = word.lower()

output = (find_word(word))

if type(output) == list:
	for item in output:
		print(item)
else:
	print(output)

if __name__ == "__main__":
	pass