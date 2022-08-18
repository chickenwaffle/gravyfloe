#!/usr/bin/env python2

import itertools
import json

def permutate(letters):
    string_permutations = itertools.permutations(letters)
    string_permutations = list(string_permutations)
    string_permutations = [''.join(permutation) for permutation in string_permutations]

    return string_permutations

def buildHashTable():
    with open('dictionaries/words_dictionary.json', 'r') as file:
        return json.load(file)


def getValidAnagrams(permutations):
    validAnagrams = {}

    for permutation in permutations:
        # "a fly dove" -> "a", "fly", "dove"
        splitPermutation = permutation.split(" ")
        for word in splitPermutation:

            # Check if current word is a valid word from our dictionary.
            if (dictionary[word] != "1"):
                break

            # Add to valid anagrams.
            validAnagrams[permutation] = 1

    return validAnagrams    

if __name__=="__main__":
    permutations = permutate("assess ")
    dictionary = buildHashTable()
    validAnagramsDict = getValidAnagrams(permutations)

    for anagram in validAnagramsDict.keys():
        print(anagram + "\n")

