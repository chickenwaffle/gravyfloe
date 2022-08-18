#!/usr/bin/env python2

f1 = open("2dict.txt","r")
f2 = open("2.txt","w")

dictionary = f1.readlines()
dictionary = [endl.strip() for endl in dictionary]

vowels     = ["a","e","i","o","u","y"]

for word in dictionary:
    print("for word in dictionary...")
    for letter in word:
        print("\tfor letter in word...")
        

        for vowel_pos in range(0, len(vowels)):
            print("\t\tfor vowel in vowels...\nletter: " + letter + "\nvowel: " + vowels[vowel_pos] + "\n")
            if letter == vowels[vowel_pos]:
                print(word)
                f2.write(word + "\n")
                break

f1.close()
f2.close()
