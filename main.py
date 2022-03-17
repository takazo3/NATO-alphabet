import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_phonetic = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    word = input("Enter a word: ").upper()

    try:
        user_word = [nato_phonetic[letter] for letter in word]

    except KeyError:
        print("Sorry, only letter in alphabet please. ")
        generate_phonetic()
    else:
        print(user_word)


generate_phonetic()