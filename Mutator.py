import re
import random

#! возможно, какие-то места возможно переписать без использования регулярки

# низкоуровневая функция кортеж из двух элементов
# первый элемент кортежа -- часть строки, не содержащая комментарий
# второй элемент кортежа -- часть строки, содержащая комментарий
# если в строке отсутствует какая-либо часть (например вся строка комментарий или строка не содержит комментарий),
#   на месте ссответствующего элемента кортежа ставится None 
def _IsLineComment(line):
    # сразу отсеиваем строки, подозрительные на сожердание комментария
    match = re.search(r'[*, /]', line)

    # обрабатываем первы случай
    if (match and (match[0] == '*' or match[0] == '/')):
        return (None, line)
    # обрабатываем второй случай
    elif (line.find('//') != -1):
        result = re.split(r'//', line)
        if (result):
            # в этом случае трока делится на 2 части: подстрока с кодом и подстрока с комментарием
            # подстроки записываются в список result, так как нам нужна подстрока с комменатрием
            # вы выбираем result[1]
            return (str(result[0]), "//" + str(result[1]))
    else:
        return (line, None)


# основная функция, получающая на вход файл и выдающая список строчек
# в которых находятся комментарии (или их части)
#! части многострочных комментариев начинаются с символа *
# пример многострочного комментария в коде на C++
'''
/*!                        
* Sum two numbers          
* \param a,b numbers       
* \return the sum of two arguments
*/
'''
def Parser(fd_src, fd_dst, loop_num):
    # получаем список строк файла
    src_lines_list = fd_src.read().splitlines()

    # обрабатываем каждую строку на присутствие в них комментариев
    # принципиально возможно 2 ситуации: 
    # всю строку занимает комментарий (или часть многострочного комментария)
    # строка содержит часть кода и комментарий
    for line in src_lines_list:
        res = _IsLineComment(line)

        # если строка содержит комментарий
        if res[1] != None:
            # мутируем комментарий
            comment_l = res[1]
            for i in range(loop_num):
                mutated = mutate(comment_l)
                comment_l = mutated

            # если вся строчка -- комментарий
            if res[0] == None:
                fd_dst.write(mutated + "\n")
            # если в строчке помимо комментария есть код
            else:
                fd_dst.write(res[0] + mutated + "\n")
        # если строка не содержит комментарий
        else:
            fd_dst.write(res[0] + "\n")

# Функции, мутирующие строчки комментариев

# удаление из строки случайного символа
def delete_random_character(s: str) -> str:
    if (s == ""):
        return s

    pos = random.randint(0, len(s) - 1)
    # print("Deleting", repr(s[pos]), "at", pos)
    return s[:pos] + s[pos + 1:]

# вставка в строку случайного символа
def insert_random_character(s: str) -> str:
    pos = random.randint(0, len(s))
    random_character = chr(random.randrange(32, 127))
    # print("Inserting", repr(random_character), "at", pos)
    return s[:pos] + random_character + s[pos:]

# своп двух рандомных символов в строке
def flip_random_character(s):
    if (s == ""):
        return s

    pos = random.randint(0, len(s) - 1)
    c = s[pos]
    bit = 1 << random.randint(0, 6)
    new_c = chr(ord(c) ^ bit)
    # print("Flipping", bit, "in", repr(c) + ", giving", repr(new_c))
    return s[:pos] + new_c + s[pos + 1:]

# функция, выбирающая случайную мутацию из списка
def mutate(s: str) -> str:
    mutators = [
        delete_random_character,
        insert_random_character,
        flip_random_character
    ]
    mutator = random.choice(mutators)
    # print(mutator)
    return mutator(s)