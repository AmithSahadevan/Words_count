Input = input("Enter a sentance: ")
my_word = input("Enter the word: ")
count = 0

new_sentence = Input.replace(".", " ")

lizt = new_sentence.split(" ")

for word in lizt:
	if word == my_word:
		count += 1

print(f"\"{my_word}\" repeats {count} time(s).")