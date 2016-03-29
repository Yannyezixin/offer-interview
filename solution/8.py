#!/usr/bin/env python
# encoding: utf-8

"""
    题目描述:
        把一个数组最开始的若干个元素搬到数组的末尾，称之为数组的旋转，
        输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素，
        例如数组{3, 4, 5, 1, 2} 为{1, 2, 3, 4, 5} 的一个旋转，该数组的最
        小元素为1, 时间复杂度要求为O(logn)
    思路:
        可用二分查找来得到， 但出现 data[first] = data[mid] = data[last]
        时， 如 [1, 0, 1, 1, 1] 无法使用二分查找，此时只能用顺序查找
"""

def solution(data):
    if not data:
        return None

    length = len(data)
    index1 = 0
    index2 = length - 1
    indexMid = index1

    while data[index1] >= data[index2]:
        if index2 - index1 == 1:
            indexMid = index2
            break
        indexMid = (index1 + index2) / 2

        if data[index1] == data[index2] and data[indexMid] == data[index1]:
            return min(data[index1:index2+1])
        if data[indexMid] >= data[index1]:
            index1 = indexMid
        else:
            index2 = indexMid

    return data[indexMid]


import unittest
class TestSolution(unittest.TestCase):

    def setUp(self):
        self.testList = [
            ([3, 4, 5, 1, 2], 1),
            ([1, 1, 1, 1, 1], 1),
            ([2, 4, 6, 8, 10], 2),
            ([1, 0, 1, 1, 1], 0),
            ([1, 1, 1, 0, 1], 0),
            ([1], 1),
            ([1, 0], 0),
            ([], None)
        ]

    def test_solution(self):
        finalResult = True
        for input, result in self.testList:
            res = solution(input)
            finalResult = finalResult == (result == res)
            if finalResult == False:
                print 'Test failed!'
                print 'input:', input
                print 'Output', res
                print 'Except', result
                break
        self.assertEquals(finalResult, True)


