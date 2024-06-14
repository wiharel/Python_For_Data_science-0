#prendre en argument la chaine de characteres
#Si aucune donnees lui est transmit lui mettre comme valeur le Hello World 
#Si le nombre d'arguments est incorrect afficher une Assertion error
#Respecter la norme de flake8
import sys
import string

def count_characters(text):
    upper_count = 0
    lower_count = 0
    punctuation_count = 0
    digit_count = 0
    space_count = 0

    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char in string.punctuation:
            punctuation_count += 1
        elif char.isdigit():
            digit_count += 1
        elif char.isspace():
            space_count += 1
    total_chars = len(text)


    print(f"The text contains {total_chars} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punctuation_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")

def main():
    if len(sys.argv) > 2:
        raise AssertionError("More than one argument is provided")

    text = sys.argv[1]

    
    count_characters(text)

if __name__ == "__main__":
    main()
