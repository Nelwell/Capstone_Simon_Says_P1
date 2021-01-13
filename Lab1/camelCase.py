# This program takes any sentence and converts it to camel case, with first word being lowercase and first letter of subsequent words capitalized

sentence = input('Write a sentence: ') # original sentence

word_list = sentence.split() # turns sentence into list of words

first_letters_capital = [] # empty list

for word in word_list: # loops through each word in word_list
    first_letters_capital.append(word.lower().title()) # appends each word with first letter capitalized

list_to_single_string = ' '.join(first_letters_capital).replace(' ', '') # converts list of strings into single string and removes white space - https://stackoverflow.com/questions/36094979/convert-a-list-of-strings-into-one-string
camel_case_sentence = list_to_single_string[0].lower() + list_to_single_string[1:] # capitalizes first letter of string - https://www.geeksforgeeks.org/python-lowercase-first-character-of-string/

print(camel_case_sentence)