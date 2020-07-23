# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 11:48:58 2020

@author: MADCAT
"""


sntnc = str(input("input your sentence:"))


def letr_count(s):
    """counts every single char in given string"""
    letr_count = dict()
    a = set(s)
    for i in a:
        letr_count[i] = s.count(i)
    return dict(sorted(letr_count.items()))


print(letr_count(sntnc))
   