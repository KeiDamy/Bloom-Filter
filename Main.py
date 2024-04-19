#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Main.py:各処理の呼び出し"""
__author__ = 'Yokokawa Kotaro'
__version__ = '1.0.0'
__date__ = '2024/04/19(Created: 2024/04/19)'

from BloomFilter import BloomFilter

if __name__ == '__main__':
    anBloomFilter = BloomFilter()
    anBloomFilter.input_data()
    anBloomFilter.hash_data()
    anBloomFilter.output_data()
    print()
    anBloomFilter.check_input()
