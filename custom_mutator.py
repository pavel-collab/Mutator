#!/usr/bin/env python3
# encoding: utf-8
"""
Кастомный мутатор для файзера AFL++ написан на основе шаблона кастомного мутатора
из официальной документации

@author: Pavel Philippenko

@license:

@contact: filippenko.ps@phystech.edu
"""

import random
import Mutator

loop_num = 50

COMMANDS = [
    b"GET",
    b"PUT",
    b"DEL",
    b"AAAAAAAAAAAAAAAAA",
]

def init(seed):
    """
    Called once when AFLFuzz starts up. Used to seed our RNG.

    @type seed: int
    @param seed: A 32-bit random value
    """
    # Seed our RNG
    random.seed(seed)

def deinit():
    pass

def fuzz(buf, add_buf, max_size):
    """
    Called per fuzzing iteration.

    @type buf: bytearray
    @param buf: The buffer that should be mutated.

    @type add_buf: bytearray
    @param add_buf: A second buffer that can be used as mutation source.

    @type max_size: int
    @param max_size: Maximum size of the mutated output. The mutation must not
        produce data larger than max_size.

    @rtype: bytearray
    @return: A new bytearray containing the mutated data
    """
    # Make a copy of our input buffer for returning

    '''
    копируем полученный массив байт в локальную переменную
    дикодируем массив байт в строку, чтобы применить к ней мутацию из модуля
    применяем функцию мутации из модуля Mutator (мутация применяется 50 раз -- переменная loop_num)
    кодируем оббратно в массив байт
    '''
    ret = bytearray(buf)
    '''
    в результате некорректного поведения метода decode
    возможна ситуация, когда будет кидаться исключение
    для обработки исключения пишем конструкцию try except
    '''
    try:
        comment_l = ret.decode(encoding='utf-8', errors='strict')
        for i in range(loop_num):
            mutated = Mutator.mutate(comment_l)
            comment_l = mutated
        ret = bytearray(mutated.encode('utf-8'))
    except UnicodeDecodeError:
        ret = bytearray(buf)

    # Return data
    return ret