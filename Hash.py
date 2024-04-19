#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Hash.py:ハッシュかを行うクラス"""
__author__ = 'Yokokawa Kotaro'
__version__ = '1.0.0'
__date__ = '2024/04/19(Created: 2024/04/19)'

import hashlib

class Hash():
    """"""
    def __init__(self, filter, filter_size):
        """"""
        self.filter = filter
        self.filter_size = filter_size

    def hash_item(self,item):
        hash_object = hashlib.sha256(item.encode())
        hash_digest = hash_object.hexdigest()
        index = int(hash_digest, 16) % self.filter_size
        return index

    def hash_data(self, data):
        for c in data:
            index = self.hash_item(c)
            self.filter[index] = 1
        return self.filter
