# Write your solution here
from random import sample, randint

def generate_strong_password(length: int, number: bool, special_char: bool):
    alphabet = list(map(chr, range(97, 123)))
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    special_characters = ["!", "?", "=", "+", "-", "(", ")", "#"]
    password_list = []

    if number == True:
        if special_char == True:
            upper_bound = min(length-2 , 10)
            num_of_num = randint(1, upper_bound)
            upper_bound2 = min(length - 1 - num_of_num , 8)
            num_of_special_char = randint(1, upper_bound2)
            num_of_letters = length - num_of_num - num_of_special_char
            password_list_num = sample(digits, num_of_num)
            password_list_special_char = sample(special_characters, num_of_special_char)
            if num_of_letters != 0:
                password_list_letter = sample(alphabet, num_of_letters)
                password_list = password_list_num + password_list_special_char + password_list_letter
            else:
                password_list = password_list_num + password_list_special_char 
        else:
            upper_bound = min(length-1 , 10)
            num_of_num = randint(1, upper_bound)
            num_of_letters = length - num_of_num
            password_list_num = sample(digits, num_of_num)
            if num_of_letters != 0:
                password_list_letter = sample(alphabet, num_of_letters)
                password_list = password_list_num + password_list_letter
            else:
                password_list = password_list_num
    else:
        if special_char == True:
            upper_bound = min(length-1 , 8)
            num_of_special_char = randint(1, upper_bound)
            num_of_letters = length - num_of_special_char
            password_list_special_char = sample(special_characters, num_of_special_char)
            if num_of_letters != 0:
                password_list_letter = sample(alphabet, num_of_letters)
                password_list = password_list_special_char + password_list_letter
            else:
                password_list = password_list_special_char
        else: 
            password_list = sample(alphabet, length)
    
    password_list = sample(password_list, length)
    password = ""
    for i in password_list:
        password += i
    return password
