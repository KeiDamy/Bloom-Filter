#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""BloomFilter:BloomFilterの管理を行う"""
__author__ = 'Yokokawa Kotaro'
__version__ = '1.0.0'
__date__ = '2024/04/19(Created: 2024/04/19)'

from IOProcess import IOProcess
from Hash import Hash

class BloomFilter:
    """"""
    def __init__(self):
        self.filter_size = 1000
        self.filter = [0] * self.filter_size
        self.iop = IOProcess()
        self.hash = Hash(self.filter, self.filter_size)
        
    def input_data(self):
        self.iop.input_data()

    def hash_data(self):
        self.filter = self.hash.hash_data(self.iop.data)
        
    def output_data(self):
        self.iop.output_data(self.filter)

    def check_input(self):
        check = input()
        check_hash = self.hash.hash_item(check)
        if self.filter[check_hash] == 1:
            print("positivity")
        else:
            print("negative")
