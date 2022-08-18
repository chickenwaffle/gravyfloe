#!/usr/bin/env python2

tuna = open("words_alpha.txt","r")
pizza = open("2dict.txt","w")

tony = tuna.readlines()

tony = [endl.strip() for endl in tony]

for word in tony:
    if len(word) == 2:
        pizza.write(word + "\n")


tuna.close()
pizza.close()
