student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#theory
#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas as pd
student_data_frame = pd.DataFrame(student_dict)

#theory
#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
data = pd.read_csv("nato_phonetic_alphabet.csv")
phonetics_dict = {row.letter: row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
#user_word = input("Enter a word").upper()
#output_list = [phonetics_dict[letter] for letter in user_word]
#print(output_list)


def generate_phonetics():
    user_word = input("Enter a word").upper()
    try:
        output_list = [phonetics_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, enters letters only...")
        generate_phonetics()
    else:
        print(output_list)

generate_phonetics()