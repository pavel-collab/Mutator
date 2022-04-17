import re
import os
import numpy as np

def Parser(file_name):
    fd = open('./testcases/h.cpp', 'r')
    if (fd == 0):
        print("Error open")
        os._exit(1)

    lines_list = fd.read().splitlines()
    print(lines_list)
    print()
    print()

    for line in lines_list:
        match = re.search(r'[*, /]', line)
        if (match and (match[0] == '*' or match[0] == '/')):
            print(line)

    fd.close()