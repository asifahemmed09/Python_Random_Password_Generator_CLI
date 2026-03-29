import utils.transport
import utils.session
import random
import string

def generate_password(min_length,numbers = True, symbols = True):
    letters = string.ascii_letters
    digits = string.digits
    punctuation = string.punctuation

    characters = letters
    if numbers:
      characters += digits
    if symbols:
       characters += punctuation
   

    password = ''
    has_number = False
    has_symbol = False
    meet_citeria = False

    while not meet_citeria or len(password) < min_length:
       character = random.choice(characters)
       password += character

       if character in digits:
          has_number = True
       elif character in punctuation:
          has_symbol = True

       meet_citeria = True
       
       if numbers:
          meet_citeria = has_number
       if symbols:
          meet_citeria = meet_citeria and has_symbol
    return password


print("Welcome to Password Generator!")
min_length = int(input("How long your password should be: "))
is_number = input("Should password include number? (y/n): ").lower() == "y"
is_symbol = input("Should password include symbols? (y/n): ").lower() == "y"

password = generate_password(min_length,is_number,is_symbol)
print(f"Your generated password is: {password}")