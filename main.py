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
        if isValidPermutation(splitPermutation):
            validAnagram = " ".join(splitPermutation)
            validAnagrams[validAnagram] = 1
    
    return validAnagrams

def isValidPermutation(permutation):
    for word in permutation:
        # Check if current word is a valid word from our dictionary.
        try:
            if (dictionary[word] == 0 and not ""):
                return False
        except KeyError:
            return False

    return True

# Print anagrams in a grid for improve readability.
def prettyPrint(permutations):
    if len(permutations) == 0:
        return ""

    output = ""
    wordsOnLine = 0
    wordPerLine = 4

    for permutation in permutations:
        # Print current char buffer then reset it.
        if wordsOnLine % wordPerLine == 0:
            print(output)
            output = ""
            wordsOnLine = 0

        if wordsOnLine == 0:
            output = permutation
        else:
            output += " | " + permutation
        
        wordsOnLine += 1

if __name__=="__main__":
    permutations = permutate("aefglorvy ")
    dictionary = buildHashTable()
    validAnagramsDict = getValidAnagrams(permutations)

    prettyPrint(validAnagramsDict.keys())