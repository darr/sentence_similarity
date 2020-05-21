#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : main.py
# Create date : 2019-08-20 15:51
# Modified date : 2020-05-21 21:36
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

from sim_cilin import SimCilin
from sim_hownet import SimHownet
from sim_simhash import SimHaming
from sim_tokenvector import SimTokenVec
from sim_vsm import SimVsm

def test_text(text1, text2):
    print("sentence1:%s" % text1)
    print("sentence2:%s" % text2)

    cilin = SimCilin()
    print('cilin', cilin.distance(text1, text2))

    hownet = SimHownet()
    print('hownet', hownet.distance(text1, text2))

    simhash = SimHaming()
    print('simhash', simhash.distance(text1, text2))

    simtoken = SimTokenVec()
    print('simtoken', simtoken.distance(text1, text2))

    simvsm = SimVsm()
    print('simvsm', simvsm.distance(text1, text2))
    print('\n')

def test():
    cilin = SimCilin()
    hownet = SimHownet()
    simhash = SimHaming()
    simtoken = SimTokenVec()
    simvsm = SimVsm()

    while 1:
        text1 = input('enter sent1:').strip()
        text2 = input('enter sent2:').strip()
        print('cilin', cilin.distance(text1, text2))
        print('hownet', hownet.distance(text1, text2))
        print('simhash', simhash.distance(text1, text2))
        print('simtoken', simtoken.distance(text1, text2))
        print('simvsm', simvsm.distance(text1, text2))

def run():
    text1 = "南昌是江西省的省会"
    text2 = "北京乃中国之首都"
    test_text(text1, text2)

    text1 = "我是中国人，我深爱着我的祖国"
    text2 = "中国是我的母亲，我热爱她"
    test_text(text1, text2)

    text1 = "一群高贵气质的差人在处罚违章动物"
    text2 = "城管执法，若不文明会导致很多不公平事故"
    test_text(text1, text2)

    text1 = "小明去了姥姥家，姥姥给他买了一本童话书"
    text2 = "我外婆早早的就出去了，给我带回来一本恐怖小说"
    test_text(text1, text2)

    #test()

run()
