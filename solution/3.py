#!/usr/bin/env python
# encoding:utf-8

"""
    题目描述：
        在一个二维数组中，每一行都从左到右递增的顺序排序，每一列都从上到下递增的
        顺序排序。请完成一个函数， 输入这样的一个二维数组和一个整数，判断数组中
        是否含有该整数
    思路:
        从右上角开始，如果当前数字大于查找整数，那么该列的数字都大于查找整数，
        那么查找目标左移一列，如果当前数组小于查找整数，那么该行数字都小于查找
        整数，目标下移一行，直到找到查找目标，否则返回False
"""

def solution(array, search):
    if array in (None, []):
        return False
    width = len(array[0])
    depth = len(array)

    if search < array[0][0]:
        return False
    if search > array[width-1][depth-1]:
        return False

    i = 0
    j = width - 1
    while j >= 0 and i < depth:
        if array[i][j] == search:
            return True
        elif array[i][j] < search:
            i += 1
        else:
            j -= 1

    return False


if __name__ == '__main__':

    array = [[1, 2, 3, 4, 5],
            [2, 3, 4, 5, 6],
            [3, 6, 9, 12, 15],
            [5, 7, 10, 13, 16],
            [6, 9, 11, 14, 18]]

    searchList = [(-2, False), (1, True), (18, True), (20, False), (8, False), (10, True)]

    finalResult = True
    for search, result in searchList:
        res = solution(array, search)
        finalResult = finalResult == (result == res)
        if finalResult == False:
            print 'Test failed!'
            print 'input:', search
            print 'Output', res
            print 'Except', result
            break
    if finalResult == True: print 'Accepted!'
