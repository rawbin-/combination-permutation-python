#!/usr/bin/env python
# -*- coding:utf-8 -*-
# =========================================================================== #
#
# @Date: 2021/12/10 10:51 AM
# @Author: zhangliao
# @Project: combination-permutation-python
# @FileName: combinations-permutations-all.py
# @Description: description for this file
#
# =========================================================================== #
from itertools import combinations,permutations

class CombPerm:
    def combinations(self,*args):
        return list(combinations(*args))

    def permutations(self,*args):
        return list(permutations(*args))



if __name__ == '__main__':
    obj = CombPerm()
    print(obj.combinations([1,2,3,4,5,6],3))
    print(obj.permutations([1,2,3,4,5,6],3))


