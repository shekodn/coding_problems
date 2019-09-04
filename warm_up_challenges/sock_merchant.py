#!/usr/bin/python3

"""
Sock Merchant

https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

Sample Input
9
10 20 20 10 10 30 50 10 20

Sample Output

3
"""

def read_input():
    val = input("Enter your value: ")
    print(val)


def array_to_dict(array):
    dict = {}
    for x in array:
        if x not in dict:
            dict[x] = 1
        else:
            dict[x] = dict[x] + 1

    return dict

def count_pairs(the_dict):
    counter = 0
    for k, v in the_dict.items():
        counter = counter + int((v / 2))
    return counter

if __name__ == "__main__":

    n = int(input())

    ar = []
    pair_count = 0
    dict_socks = {}

    numbers = input()
    ar = numbers.split(' ')
    dict_socks = array_to_dict(ar)
    pair_count = count_pairs(dict_socks)
    print(pair_count)
