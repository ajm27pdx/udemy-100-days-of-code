import pandas
# # Exceptions
#
#
# try:
#     file = open('file.txt')
#     a_dictionary = {'key': 'value'}
#     print(a_dictionary['fjw'])
# except FileNotFoundError:
#     file = open('file.txt', 'w')
# except KeyError as error_message:
#     print(f'{error_message} not found')
# else:
#     content = file.read()
# finally:
#     file.close()
#
# # Raise
# raise KeyError

# Improve NATO Alphabet app with error handling
alpha_data = pandas.read_csv('nato_phonetic_alphabet.csv')
alphabet_dict = {row.letter: row.code for (index, row) in alpha_data.iterrows()}
# print(alphabet_dict)
valid_input = False
while not valid_input:
    user_input = [*input("Enter a word: ").upper()]
    try:
        output_list = [alphabet_dict[letter] for letter in user_input]
    except KeyError:
        print('Sorry, only letters are valid')
    else:
        valid_input = True


print(output_list)