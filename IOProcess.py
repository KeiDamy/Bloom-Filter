#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""IOprocess.py:入出力管理"""
__author__ = 'Yokokawa Kotaro'
__version__ = '1.0.0'
__date__ = '2024/04/19(Created: 2024/04/19)'


class IOProcess():
    """"""
    def __init__(self):
        self.data = []

    def input_data(self):
        while True:
            char = input()
            if char == 'end': break
            self.data.append(char)
        return self.data

    def output_data(self, filter):
        for i in filter:
            print(i,end=",")
