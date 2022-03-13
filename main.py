import pandas


data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_phonetic = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()
user_word = [nato_phonetic[letter] for letter in word]

print(user_word)
