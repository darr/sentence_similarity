#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : sim_vsm.py
# Create date : 2019-08-20 16:33
# Modified date : 2020-05-21 10:43
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

import jieba.posseg as pesg
import math
import numpy as np

class SimVsm:

    def distance(self, text1, text2):
        '''比较相似度'''
        words1 = [word.word for word in pesg.cut(text1) if word.flag[0] not in ['u', 'x', 'w']]
        words2 = [word.word for word in pesg.cut(text2) if word.flag[0] not in ['u', 'x', 'w']]
        tfidf_reps = self.tfidf_rep([words1, words2])
        return self.cosine_sim(np.array(tfidf_reps[0]), np.array(tfidf_reps[1]))

    def tfidf_rep(self, sents):
        '''对句子进行tfidf向量表示'''
        sent_list = []
        df_dict = {}
        tfidf_list = []
        for sent in sents:
            tmp = {}
            for word in sent:
                if word not in tmp:
                    tmp[word] = 1
                else:
                    tmp[word] += 1
            tmp = {word:word_count/sum(tmp.values()) for word, word_count in tmp.items()}
            for word in set(sent):
                if word not in df_dict:
                    df_dict[word] = 1
                else:
                    df_dict[word] += 1
            sent_list.append(tmp)
        df_dict = {word :math.log(len(sents)/df+1) for word, df in df_dict.items()}
        words = list(df_dict.keys())
        for sent in sent_list:
            tmp = []
            for word in words:
                tmp.append(sent.get(word, 0))
            tfidf_list.append(tmp)
        return tfidf_list

    def cosine_sim(self, vector1, vector2):
        '''余弦相似度计算相似度'''
        cos1 = np.sum(vector1 * vector2)
        cos21 = np.sqrt(sum(vector1 ** 2))
        cos22 = np.sqrt(sum(vector2 ** 2))
        similarity = cos1 / float(cos21 * cos22)
        return similarity

def test():
    text1 = '南昌是江西的省会'
    text2 = '北京乃中国之首都'

    text1 = '周杰伦是一个歌手'
    text2 = '刘若英是个演员'

    simer = SimVsm()
    sim = simer.distance(text1, text2)
    print(sim)

#test()
