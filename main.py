#!/usr/bin/env python3
from sys import argv, exit
import os
import Mutator

def main():

    # можно мутировать заданный файл
    if len(argv) == 2:
        FILE_NAME = argv[1]
        
        # открываем файл и проверям успешность открытия
        fd_src = open(FILE_NAME, 'r')
        if (fd_src == -1):
            print("Error open")
            exit(1)

        fd_dst = open("mutated_" + FILE_NAME, 'w')
        if (fd_dst == -1):
            print("Error open")
            exit(1)

        Mutator.Parser(fd_src, fd_dst)
        fd_dst.close()
        fd_src.close()
    # или мутировать все файлы из указанной дериктории (дефолтный режим работы)
    else:
        DIR_NAME = "./testcases/"

        # переменная хранит названия файлов в testcases
        dirfiles = os.listdir(DIR_NAME) 

        for file in dirfiles:
            FILE_NAME = file

            # открываем файл и проверям успешность открытия
            fd_src = open(DIR_NAME + FILE_NAME, 'r')
            if (fd_src == -1):
                print("Error open")
                exit(1)

            fd_dst = open("mutated_" + FILE_NAME, 'w')
            if (fd_dst == -1):
                print("Error open")
                exit(1)

            Mutator.Parser(fd_src, fd_dst)
            fd_dst.close()
            fd_src.close()

if __name__ == '__main__':
    main()