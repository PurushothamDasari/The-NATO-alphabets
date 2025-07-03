import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary in this format:
nato_phonetic_dict = {row.letter:row.code for (index, row) in df.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
def create_nato_phonetic():
    word = input("Enter a word: ").upper()
    try:
        nato_phonetic_list = [nato_phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in alphabets are allowed. Please kindly enter a valid word.")
        create_nato_phonetic()
    else:
        print(nato_phonetic_list)
create_nato_phonetic()
