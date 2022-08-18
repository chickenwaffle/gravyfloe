#!/usr/bin/env python2

import itertools

def permutate(letters):
    string_permutations = itertools.permutations(letters)
    string_permutations = list(string_permutations)
    string_permutations = [''.join(permutation) for permutation in string_permutations]

    return string_permutations
