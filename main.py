#!/usr/bin/env python3
from sys import argv, exit
import os
import Mutator
import re

def main():

    DIR_NAME = "./testcases/"
    FILE_NAME = "h.cpp"

    if len(argv) == 2:
        FILE_NAME = argv[1]
    if len(argv) == 3:
        FILE_NAME = argv[1] if argv[1] != '*' else "h.cpp"
        DIR_NAME = argv[2] if argv[2] != '*' else "./testcases/"

    # переменная хранит названия файлов в testcases
    dirfiles = os.listdir(DIR_NAME) 
    buf = Mutator.Parser(DIR_NAME, FILE_NAME)

    print("Without mutation:")
    for item in buf:
        print(item)

    print()
    print("Mutation -- delete random character:")
    for item in buf:
        print(Mutator.delete_random_character(item))

    print()
    print("Mutation -- insert random character:")
    for item in buf:
        print(Mutator.insert_random_character(item))

    print()
    print("Mutation -- flip random character:")
    for item in buf:
        print(Mutator.flip_random_character(item))

    # print()
    # print("Mutation random mutation:")
    # for item in buf:
    #     print(Mutator.mutate(item))

if __name__ == '__main__':
    main()