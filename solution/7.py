#!/usr/bin/env python
# encoding: utf-8

"""
    题目描述:
        用两个栈来实现一个队列, 并实现两个函数appendTail, deleteHead, 分别完成
        在队列尾部插入结点和在队列头删除结点的功能
    思路:
        栈1用来存放元素， 栈2用来出栈, 入队列时直接把元素入栈到栈1，
        出队列时，如果栈2为空，遍把栈1全部出栈并入栈到栈2, 栈2再出栈

"""

class Queue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, x):
        self.stack1.append(x)

    def deleteHead(self):
        if self.stack2 == []:
            while self.stack1 != []:
                self.stack2.append(self.stack1.pop())

        if self.stack2 == []:
            return False
        else:
            return self.stack2.pop()

import unittest

class TestQueue(unittest.TestCase):

    def setUp(self):
        self.testList = [
            (['abcdef', 'c', 'd'], ['abcdef', 'c', 'd']),
            ([1212], [1212]),
            ([None], [None])
        ]

    def test_case(self):
        finalResult = True
        for input, output in self.testList:
            queue = Queue()
            map(queue.appendTail, input)
            res = []
            while True:
                elem = queue.deleteHead()
                if elem != False:
                    res.append(elem)
                else:
                    break
            queue.appendTail('abc')
            output.append('abc')
            res.append(queue.deleteHead())
            finalResult = finalResult == (output == res)
            if finalResult == False:
                print 'Test failed!'
                print 'input:', input
                print 'Output', res
                print 'Except', output
                break
        # if finalResult == True: print 'Accepted!'
        self.assertEquals(finalResult, True)
