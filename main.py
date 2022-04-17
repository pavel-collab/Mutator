#!/usr/bin/env python3
from sys import argv
import os
import Mutator
import re
# char* str; ///< Brief documentation for curent object
def main():

    DIR_NAME = "./testcases/"
    if len(argv) == 2:
        DIR_NAME = argv[1]

    dirfiles = os.listdir(DIR_NAME) # переменная хранит названия файлой testcases
    # print(list(dirfiles)) # выводим все файлы в дериктории testcases

    Mutator.Parser(DIR_NAME, 'h.cpp')

if __name__ == '__main__':
    main()