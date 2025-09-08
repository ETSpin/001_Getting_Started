#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
File: main.py
Author: MORS
Date: 8 Sep 25

Description:
Working my way through the Python Crash Course Book

Usage:
N/A

"""


def main():
    first_name = "ada's"
    last_name = "lovelace"
    white_space = "test "
    full_name = f"{first_name} {last_name}"
    print(f"Hello, {full_name.title()}!")
    print(white_space.strip())

    #Lists
    bicycles = ['trek', 'canondale', 'redline', 'specialized']
    print(bicycles)
    print("First element in bicycles: ", bicycles[0])
    print("The last element in bicycles", bicycles[-1])
    bicycles.append('schwinn')
    print("You can Append to the list: ", bicycles)
    bicycles.insert(0, 'huffy')
    print("You can Insert things into the list - where you need them: ", bicycles)
    del bicycles[1]
    print("You can Delete things from the list: ", bicycles)
    popped_bicycle = bicycles.pop()
    print("You can Pop things from the end of the list: ", popped_bicycle)
    print(bicycles)
    popped_bicycle = bicycles.pop(1)
    print("You can Pop things from anywhere on the list: ", popped_bicycle)
    print(bicycles)

if __name__ == '__main__':
    main()
