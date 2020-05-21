#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : sim_simhash.py
# Create date : 2019-08-20 16:31
# Modified date : 2020-05-21 10:42
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

from simhash import Simhash
import jieba.posseg as pseg

class SimHaming:

    def haming_distance(self, code_s1, code_s2):
        '''利用64位数，计算海明距离'''
        x = (code_s1 ^ code_s2) & ((1 << 64) - 1)
        ans = 0
        while x:
            ans += 1
            x &= x - 1
        return ans

    def get_similarity(self, a, b):
        '''利用相似度计算方式,计算全文编码相似度'''
        if a > b :
            return b / a
        else:
            return a / b

    def get_features(self, string):
        '''对全文进行分词,提取全文特征,使用词性将虚词等无关字符去重'''
        word_list=[word.word for word in pseg.cut(string) if word.flag[0] not in ['u','x','w','o','p','c','m','q']]
        return word_list

    def get_distance(self, code_s1, code_s2):
        '''计算两个全文编码的距离'''
        return self.haming_distance(code_s1, code_s2)

    def get_code(self, string):
        '''对全文进行编码'''
        return Simhash(self.get_features(string)).value

    def distance(self, s1, s2):
        '''计算s1与s2之间的距离'''
        code_s1 = self.get_code(s1)
        code_s2 = self.get_code(s2)
        similarity = (100 - self.haming_distance(code_s1,code_s2)*100/64)/100
        return similarity

def test():
    text1 = '我喜欢你'
    text2 = '我讨厌你'
    simer = SimHaming()
    sim = simer.distance(text1, text2)
    print(sim)

#test()
