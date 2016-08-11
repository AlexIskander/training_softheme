#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Задача: Найти максимальную сумму пути от вершины до основания  треугольника
"""

max_sum = 0

def split_add(string):
    """находим максимальное число в строке треугольника"""
    arr = string.split(" ")
    return max(arr)

def find_max_sum(file_name):
    global max_sum
    with open(file_name, "r") as file_:
        for string in file_:
        	try:
        		max_sum += int(split_add(string))
        	except ValueError:
        		print "ValueError", string
        

if __name__ == "__main__":
    find_max_sum("data2")
    print max_sum
    
