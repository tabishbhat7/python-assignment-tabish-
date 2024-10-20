alphabets="QWERTYUIOPASDFGHJKLZXCVBNMabcdefghijklmnopqrstuvwxyz"
character=input("Enter a alphabet")
if character in alphabets:
    print(f"{character} is an  alphabet")
else:
    print(f"{character} is not an alphabet")