#!/bin/python3
"""
Bubble Sort
41 73 89 7 10 1 59 58 84 77 77 97 58 1 86 58 26 10 86 51

5 2 3 1 4
"""
def bubble_sort(the_list):

    tail = len(the_list) - 1
    left_ptr = 0
    right_ptr = 1

    for i in range(tail):
        print("i", i)
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
    the_list = n.split(' ')
    ordered_list = bubble_sort(the_list)
    print(ordered_list)
