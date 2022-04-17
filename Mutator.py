#!/usr/bin/env python3
import re
import os
import numpy as np

# возможно, какие-то места возможно переписать без использования регулярки

def Parser(testcases_dir, file_name):
    fd = open(testcases_dir + file_name, 'r')
    if (fd == 0):
        print("Error open")
        os._exit(1)

    lines_list = fd.read().splitlines()
    # print(lines_list)

    comment_lines = []

    for line in lines_list:
        match = re.search(r'[*, /]', line)

        if (match and (match[0] == '*' or match[0] == '/')):
            comment_lines.append(line)
            # print(line)
        elif (line.find('//') != -1):
            # print(line)
            result = re.split(r'//', line)
            if (result):
                comment_lines.append("//" + str(result[1]))
    
    # print(comment_lines)
    for i in comment_lines:
        print(i)

    fd.close()