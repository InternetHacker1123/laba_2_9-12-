#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from timeit import timeit

# Выполнение функций без использования интроспекции стека.


def factorial(n):
    # Функция для вычисления факториала.
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def fib(n):
    # Функция для чисел фибоначчи.
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

# Выполнение функций с использованием интроспекции стека.


def factorial_tail(n, acc=1):
    if n == 0:
        return acc
    else:
        return factorial_tail(n - 1, acc * n)


def fib_tail(n, a=0, b=1):
    if n == 0:
        return a
    else:
        return fib_tail(n - 1, b, a + b)
