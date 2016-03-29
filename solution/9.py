#!/usr/bin/env python
#encoding:utf-8

"""
    问题描述:
        斐波那契数列
        实现一个类， 可通过键值访问， 第n个斐波那契数, 也可通过切片方式
        访问, 例如
        ```
            fib = Fib()
            fib[3] # 2
            fib[0:5] #[0, 1, 1, 2, 3]
        ```

"""

class Fib(object):

    def __init__(self):
        self._fib = [0, 1]
        self._len = 2

    def __getitem__(self, n):
        if isinstance(n, int):
            if n < self._len:
                return self._fib[n]

            for i in xrange(self._len - 1, n):
                self._fib.append(self._fib[i] + self._fib[i - 1])
                self._len += 1

            return self._fib[n]
        if isinstance(n, slice):
            start = n.start
            stop = n.stop

            if not isinstance(stop, int):
                raise ValueError('stop value type must be int')

            if stop > self._len - 1:
                for i in xrange(self._len - 1, stop - 1):
                    self._fib.append(self._fib[i] + self._fib[i - 1])
                    self._len += 1

            return self._fib[start:stop]

import unittest

class TestFib(unittest.TestCase):

    def test_fib_n(self):
        fib = Fib()
        self.assertEquals(fib[0], 0)
        self.assertEquals(fib[1], 1)
        self.assertEquals(fib[2], 1)
        self.assertEquals(fib[3], 2)
        self.assertEquals(fib[4], 3)
        self.assertEquals(fib[5], 5)
        self.assertEquals(fib[6], 8)
        self.assertEquals(fib[7], 13)

    def test_fib_slice(self):
        fib = Fib()
        self.assertEquals(fib[:4], [0, 1, 1, 2])
        self.assertEquals(fib[4], 3)

