#!/bin/python3

"""
Sort an array without changing position of negative numbers

Reference:
https://www.geeksforgeeks.org/sort-an-array-without-changing-position-of-negative-numbers/

Input: 2, -6, -3, 8, 4, 1
Output: 1 -6 -3 2 4 8

Input: -2, -6, -3, -8, 4, 1
Output: -2 -6 -3 -8 1 4

"""


def bubble_sort(the_list):

    tail = len(the_list) - 1
    left_ptr = 0
    right_ptr = 1

    for i in range(tail):
        while(right_ptr <= tail):
            if the_list[left_ptr] > the_list[right_ptr]:
                aux = the_list[right_ptr]
                the_list[right_ptr] = the_list[left_ptr]
                the_list[left_ptr] = aux
            left_ptr+=1
            right_ptr+=1
        left_ptr = 0
        right_ptr = 1
        tail-=1

    return the_list


if __name__ == "__main__":
    n = input()

    the_list = n.split(',')

    number_list = list(map(int, the_list))
    negative_dict = {}
    positive_list = []

    for i in range(len(number_list)):
        if number_list[i] < 0:
            negative_dict[i] = number_list[i]
        else:
            positive_list.append(number_list[i])


    sorted_positive_list = bubble_sort(positive_list)

    for k, v in negative_dict.items():
        sorted_positive_list.insert(k,v)

    print(sorted_positive_list)
