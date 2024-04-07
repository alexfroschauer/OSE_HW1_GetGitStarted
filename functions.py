# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 21:20:56 2024

@author: froscale
"""

def isNaturalNumber(number):
    if (number * 10) % 10 == 0:
        return True
    else:
        return False

def isPrimeNumber(number):
    if isNaturalNumber(number) == True: 
        if number == 2:
            return True
        i = 2
        count = 0
        while i < number - 1:
            if number % i == 0:
                count += 1
                if count == 1:
                    return False
            i += 1
        return True
    else:
        return False