#!/usr/bin/env python
# -*- coding:utf-8 -*-
# =========================================================================== #
#
# @Date: 2021/12/8 11:42 AM
# @Author: zhangliao
# @Project: combination-permutation-python
# @FileName: combinations
# @Description: description for this file
#
# =========================================================================== #


from itertools import combinations
import string
setA = range(1,7)  # [1,2,3,4,5,6]
setB = list(string.ascii_uppercase[0:6]) # ['A','B','C','D','E','F']
resultA = []
resultB = []

for i in range(len(setA) + 1):
    resultA += combinations(setA,i)
print(resultA)

for i in range(len(setB) + 1):
    resultB += combinations(setB,i)
print(resultB)