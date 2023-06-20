#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('Input/Names/invited_names.txt', mode='r') as f:
    names = f.readlines()

clean_names = []
for name in names:
    clean_name = name.strip()
    clean_names.append(clean_name)

with open('Input/Letters/starting_letter.txt', mode='r') as f:
    sample_letter = f.read()

for name in clean_names:
    final_letter = sample_letter.replace('[name]', name)
    out_string = 'Output/ReadyToSend/' + name + '_letter.txt'
    with open(out_string, mode='w') as f:
        f.write(final_letter)
