print("hello world")
def count_words(words):
	return len(words.split())

def count_letters(words):
	dict = {}
	lower = words.lower()
	stripped = lower.strip()
	for letter in stripped:
		if letter in dict:
			dict[letter] += 1
		else:
			dict[letter] = 1

	return dict

def report(dict, count):
	items = dict.items()
	sorted = list(items)
	sorted.sort(key=lambda a: a[1], reverse=True)
	print("--- Begin report of books/frankenstein.txt ---")
	print(f"{count} words found in file")
	for char in sorted:
		if char[0].isalpha():
			print(f"The '{char[0]}' character appears {char[1]} times.")
	print("--- End report of books/frankenstein.txt ---")

with open("./books/frankenstein.txt") as f:
		file_contents = f.read()
		new = file_contents.replace('\n', ' ')
		word_count = count_words(new)
		count_dict = count_letters(new)
		report(count_dict, word_count)

