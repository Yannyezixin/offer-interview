#!/usr/bin/env python
# encoding:utf-8

"""
    题目描述:
        请实现一个函数，把字符串中的每个空格替换成"%20", 例如输入"We are happy",
        则输出 "We%20are%20happy".  时间复杂度要求O(n), 不得使用Python自身实现的
        字符换替换函数
    思路:
        1. 首先遍历一遍字符串，计算出空格数， 一个空格替换成"%20", 长度增加2，多少个
        空格，那么字符串就增加多少长度 X 2。
        2. 利用两个指针，P1 首先指向最后一个字符串， P2 指向字符串变更后的长度，
           移动P1, 逐个把P1指向的字符串复制到P2指向的字符串，每复制完一个，
           P1, P2都向左移动
        3. 当遇到字符串时, 至对应的把P2指向的替换成 "0", "2", "%", 替换完成判断
           此时P1 与P2 是否相同, 不同则重复第2， 3部，相同则结束替换
"""

def solution(string):
    spaceNums = 0
    for i in string:
        if i == ' ': spaceNums += 1

    if spaceNums == 0:
        return string

    string = list(string)
    newLength = len(string) + spaceNums * 2
    string.extend([' '] * spaceNums * 2)

    p2 = newLength - 1
    p1 = p2 - spaceNums * 2
    while p1 != p2:
        if string[p1] == ' ':
            string[p2] = '0'
            string[p2 - 1] = '2'
            string[p2 - 2] = '%'
            p2 -= 3
            p1 -= 1
        else:
            string[p2] = string[p1]
            p2 -= 1
            p1 -= 1

    return ''.join(string)


if __name__ == '__main__':

    testList = [
        ('abc cef', 'abc%20cef'),
        ('11 11', '11%2011'),
        ('gg ss ss ss ', 'gg%20ss%20ss%20ss%20'),
        ('ssss', 'ssss'),
        ('   ', '%20%20%20')
    ]


    finalResult = True
    for string, result in testList:
        res = soluction(string)
        finalResult = finalResult == (result == res)
        if finalResult == False:
            print 'Test failed!'
            print 'input:', string
            print 'Output', res
            print 'Except', result
            break
    if finalResult == True: print 'Accepted!'
