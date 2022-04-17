import os
import Mutator

def main():
    DIR_NAME = "./testcases/"

    dirfiles = os.listdir(DIR_NAME) # переменная хранит названия файлой testcases
    print(list(dirfiles)) # выводим все файлы в дериктории testcases

    Mutator.Parser('./testcases/h.cpp')

if __name__ == '__main__':
    main()