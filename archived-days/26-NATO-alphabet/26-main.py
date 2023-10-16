from random import randint
import pandas

# # List Comprehension
# numbers = [1, 2, 3]
# new_numbers = [n + 1 for n in numbers]
# print(new_numbers)
# print([n * 2 for n in range(1, 5) if n % 2])
#
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
#
# print([name for name in names if len(name) < 5])
# print([name.upper() for name in names if len(name) > 5])

# # Dict Comprehension
# student_scores = {student: randint(1, 101) for student in names}
# print(student_scores)
# passed_grades = {student: score for (student, score) in student_scores.items() if score > 59}
# print(passed_grades)

# Main Program - NATO Alphabet
# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
alpha_data = pandas.read_csv('nato_phonetic_alphabet.csv')
alphabet_dict = {row.letter: row.code for (index, row) in alpha_data.iterrows()}
# print(alphabet_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = [*input("Enter a word: ").upper()]
output_list = [alphabet_dict[letter] for letter in user_input]

print(output_list)
print(type(alpha_data))