#!/usr/bin/env python
# encoding: utf-8

"""
    题目描述：
        从尾到头打印链表， 不可改变原来链表的结构

    思路:
        1. 非递归, 可借助一个栈来从头到尾存放结点，出栈则是从尾到头
        2. 递归
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def initList(listVal):
    if listVal == None or listVal == []:
        return None

    dummy = ListNode(0)
    head = dummy
    for val in listVal:
        node = ListNode(val)
        head.next = node
        head = head.next

    return dummy.next

def solution_iteratively(head):
    """非递归"""
    if head == None: return None
    stack = []
    while head:
        stack.append(head)
        head = head.next

    result = ''
    while stack:
        node = stack.pop()
        result += node.val

    return result

def solution_recursively(head):
    """递归"""
    if head != None:
        tmp = solution_iteratively(head.next)
        result = tmp if tmp != None else ''
        result += head.val
        return result
    else:
        return None

if __name__ == '__main__':

    testList = (
        ('abcdef', 'fedcba'),
        ('bbbbbcc', 'ccbbbbb'),
        (None, None),
        ('1112', '2111')
    )

    finalResult = True
    for string, result in testList:
        res = solution_iteratively(initList(string))
        # res = solution_recursively(initList(string))
        finalResult = finalResult == (result == res)
        if finalResult == False:
            print 'Test failed!'
            print 'input:', string
            print 'Output', res
            print 'Except', result
            break
    if finalResult == True: print 'Accepted!'
