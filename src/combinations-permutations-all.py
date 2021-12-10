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
    @staticmethod
    def combinations(*args):
        return list(combinations(*args))
    @staticmethod
    def permutations(*args):
        return list(permutations(*args))

if __name__ == '__main__':
    print(CombPerm.combinations([1,2,3,4,5,6],3))
    print(CombPerm.permutations([1,2,3,4,5,6],3))


