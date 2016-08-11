#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Задача: Найти все числа circular prime в диапазоне от 1 до 1 миллиона? 
"""


def resheto(n = 10):
    """ Находим все простые числа в заданном диапазоне"""
    list_numbers = range(n+1)
    list_numbers[1] = 0
    lst = []
    for k in xrange(len(list_numbers)):
        if list_numbers[k] != 0:
            lst.append(list_numbers[k])
            for j in xrange(k, n+1, k):
                list_numbers[j] = 0
    return lst


def rotate(number_str):
    """ циклически сдвигаем число и записываем все значения в множество"""
    shufle=[]
    for i in range(len(number_str)):
        shufle.append(int(number_str[i:]+number_str[:i]))
    return set(shufle)

def curcle_prime(lst):
    """находим все circular prime"""
    curcle_list  = []
    # удаляем все простые числа в которых есть цифры '0','2','4', '5', '6','8'
    reject_list=['0','2','4', '5', '6','8']
    lst=[i for i in lst if not any(j in reject_list for j in set(str(i)))]
    
    while lst:
        shufle_set=rotate(str(lst[-1]))
        primes_set=set(lst)
        if not shufle_set -  primes_set:
            curcle_list+=list(shufle_set)
        lst=list(primes_set-shufle_set)
    curcle_list += [2,5]     
    curcle_list.sort()
    print len(curcle_list)
    return curcle_list

   
if __name__ == "__main__":
    lst = resheto(1000000)
    print curcle_prime(lst) 