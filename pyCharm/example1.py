#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import lru_cache

# Выполнение функций без использования декоратора.

def factorial_iterable(n):
    # Итеративная версия функции factorial.
    multiply = 1
    while n > 1:
        multiply *= n
        n -= 1
    return multiply


def fib_iterable(n):
    # Итеративная версия функции fib.
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a


# Выполнение функций с использованием декоратора.

# @lru_cache
def factorial_recursion(n):
    # Рекурсивная версия функции factorial.
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial_recursion(n - 1)


# @lru_cache
def fib_recursion(n):
    # Рекурсивная версия функции fib.
    if n == 0 or n == 1:
        return n
    else:
        return (fib_recursion(n - 2) +
                fib_recursion(n - 1))



