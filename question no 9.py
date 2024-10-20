alphabet='abcdefghijklmnopqrstuvwxyz'
digit='0123456789'
specialcharacter='~','!','@','#','$','^','&','*','(',')'
character = input("Enter a character: ")
if character in alphabet:
    print(character, "is an alphabet.")
elif character in digit:
    print(character, "is a digit.")
elif character in specialcharacter:
    print(character, "is a special character.")
else:
    print("Invalid input. Please enter a single character.")
