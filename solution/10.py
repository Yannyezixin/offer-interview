#!/usr/bin/env python
# encoding: utf-8

"""
描述:
    请实现一个函数，输入一个整数， 输出该数二进制表示中的1的个数。
    例如把9表示成二进制1001， 有2位是1。如果输入9就输出2

思路：
    把一个整数减去1, 再和原整数做与运算，可以把整数最右边的一个1变成0,有多少个1，便可以做多少次这样的操作
    C++ 次思路没问题， Python 上问题(负数会出现死循环)
"""

def solution(n):
    count = 0
    while n:
        count += 1
        n &= (n -1)

    return count

import unittest

class TestBinary(unittest.TestCase):

    def testSolution(self):
        testList = [
            (9, 2),
            (10, 2),
            (8, 1)
        ]
        finalResult = True
        for inp, out in testList:
            res = solution(inp)
            finalResult = finalResult == (out == res)
            if finalResult == False:
                print 'Test failed!'
                print 'input:', inp
                print 'Output', out
                print 'Except', res
                break
        if finalResult == True: print 'Accepted!'
        self.assertEquals(res, out)
