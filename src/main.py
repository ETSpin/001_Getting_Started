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

if __name__ == '__main__':
    main()
