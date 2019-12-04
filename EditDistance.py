# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 14:50:44 2019

@author: wuzhe
"""
import numpy as np
import editdistance
import math


"""
author: zhenyu wu
time: 2019/12/03 15:41
function: 编辑距离计算函数
params: 
    str1: 字符串1
    str2：字符串2
return:
    两个字符串之间的编辑距离
    两个字符串的相似度计算结果
"""
def edit_distance(str1, str2):
    m, n = len(str1), len(str2)
    if m==0 and n!=0:
        return n, 1-n/max(m, n)
    elif m!=0 and n==0:
        return m, 1-m/max(m, n)
    elif m==0 and n==0:
        try:
            1-0/0
        except ZeroDivisionError as z:
            print("两个字符串不能同时为空")
        return math.nan, math.nan
    else:
        d = np.zeros((n+1, m+1))
        d[0] = np.arange(m+1)
        d[:, 0] = np.arange(n+1)
        for i in range(1, n+1):
            for j in range(1, m+1):
                if str1[j-1]==str2[i-1]:
                    temp = 0
                else:
                    temp = 1
                d[i, j] = min(d[i-1, j]+1, d[i, j-1]+1, d[i-1, j-1]+temp)
        return d[n, m], 1-d[n, m]/max(m, n)
        
        
if __name__ == '__main__':
    str1 = '1010101010000101000010011001010101101'
    str2 = '101010111010101010111101010'
    dist, result = edit_distance(str1, str2)
    print('My Algorithm - Edit Distance: %.0f, Similarity: %f' % (dist, result))
    dist = editdistance.distance(str1, str2)
    print('Python Package - Edit Distance: %.0f, Similarity: %f' % (dist, 1-dist/max(len(str1), len(str2))))
