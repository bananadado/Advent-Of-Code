# "stolen" from zadukk (i have permission)
# realised after day 4 that i really shouldn't be writing out a dirs table...
import re


def extract_integers(input_string, allow_negative=False):
    pattern = r'-?\d+' if allow_negative else r'\d+'
    integers = re.findall(pattern, input_string)
    integers = [int(num) for num in integers]

    return integers


def is_character_in_column(grid, column_index, target_character):
    for row in grid:
        if row[column_index] == target_character:
            return True
    return False


def replace_character_at_index(input_string, index, new_char):
    string_list = list(input_string)
    string_list[index] = new_char
    return ''.join(string_list)


vectorsD = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (1, 1), (1, -1), (-1, 1)]
vectors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
diagonals = [(-1, 1), (1, 1), (-1, -1), (1, -1)]
dirs = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}


numsAsWords = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

#from template import *
#with open("input.txt","r") as f:
#    inp = [line.strip() for line in f.readlines()]

# useful imports
# from collections import defaultdict, deque, Counter
# import networkx as nx
# from functools import cache, cmp_to_key
# from itertools import combinations, permutations, count
# from time import perf_counter