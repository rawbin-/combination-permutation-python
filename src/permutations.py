#!/usr/bin/env python
# -*- coding:utf-8 -*-
# =========================================================================== #
#
# @Date: 2021/12/8 11:51 AM
# @Author: zhangliao
# @Project: combination-permutation-python
# @FileName: permutations
# @Description: description for this file
#
# =========================================================================== #

from itertools import permutations
import string
setA = range(1,7)  # [1,2,3,4,5,6]
setB = list(string.ascii_uppercase[0:6]) # ['A','B','C','D','E','F']

print(list(permutations(setA,3)))
print(list(permutations(setB,3)))