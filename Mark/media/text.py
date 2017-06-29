import string,random


vowels="aeiou"
consonants="bcdfghjklmnpqrstvxyz"
letters=string.ascii_lowercase


letter1=input("What letter do you want ? 'v' for Vowels,'c' for Consonants,'l' for any Letter: ")
letter2=input("What letter do you want ? 'v' for Vowels,'c' for Consonants,'l' for any Letter: ")
letter2=input("What letter do you want ? 'v' for Vowels,'c' for Consonants,'l' for any Letter: ")


def generator():
    if letter1=='v':
        print(random.choice(vowels))
    elif letter1=='c':
        print(random.choice(consonants))
    elif letter1=='l':
        print(random.choice(letters))
    else:
        print(letter1)

    if letter2=='v':
        print(random.choice(vowels))
    elif letter2=='c':
        print(random.choice(consonants))
    elif letter2=='l':
        print(random.choice(letters))
    else:
        print(letter2)

    if letter2=='v':
        print(random.choice(vowels))
    elif letter2=='c':
        print(random.choice(consonants))
    elif letter2=='l':
        print(random.choice(letters))
    else:
        print(letter2)

generator()