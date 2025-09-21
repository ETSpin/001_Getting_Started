#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
File: main.py
Author: MORS
Date: 8 Sep 25

Description:
Working my way through the Python Crash Course Book.
I will go the first bunch of chapters and then create a 
new project for the book projects.


Usage:
N/A

"""  # noqa: E501


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
    
    magicians = ['alice', 'david', 'carolina']
    for magician in magicians:
        print(magician.title())

    for value in range(5):
        print (value)

    numbers = list(range(1,6))
    even_numbers= list(range(2,11,2))
    print(numbers, "\n", even_numbers, "\n")

    '''
    earlier example
    squares = []
        for num in range(1,11):
            squares.append(num ** 2)
    squares = [value**2 for value in range(1, 11)]
    '''

    squares = [value **2 for value in range(1,11)] #comprehension method
    print(squares)
    print("The min is: ", min(squares))
    print("The max is: ", max(squares))
    print("The sum is: ", sum(squares))
    print("----------------------\n")
    print("Try it yourself exercises on page 60\n")
    print("4-4, curious how long this will take to run?")
    million = list(range(1,1000001))
    print(million)
    print("The min is: ", min(million))
    print("The max is: ", max(million))
    print("The sum is: ", sum(million))
    print("\n4-9, list comprehension")
    cubes = [num **3 for num in range(1,11)]
    print(cubes)
    print("----------------------\n")

    newcubes = cubes[:] #To copy a list you need to use a slice (of the entire list)
    newcubes2 = cubes #All this does does is set the new list "pointer" to the same 
                      #place as the old list -- so they will always show the same info

    cubes.append(0)

    print(cubes)
    print(newcubes)
    print(newcubes2)
    print("----------------------\n")
    
    newcubes2.append(3)
    print(cubes)
    print(newcubes2)

if __name__ == '__main__':
    main()
