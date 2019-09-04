#!/usr/bin/python3
"""
https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
--------------------------------------------------------------------------------
Sample Input 0
7
0 0 1 0 0 1 0

Sample Output 0
4
--------------------------------------------------------------------------------
Sample Input 1
6
0 0 0 0 1 0

Sample Output 1
3
--------------------------------------------------------------------------------
Sample Input 2
7
0 0 0 0 0 0 0

Sample Output 2
3
--------------------------------------------------------------------------------
Sample Input 3
7
0 0 0 0 0 0 0

Sample Output 3
1
--------------------------------------------------------------------------------
"""

def can_jump(number_of_steps, array, index):
    if len(array) > index + number_of_steps:
        return True
    return False


if __name__ == "__main__":

    arr_size = int(input())
    numbers = input()
    arr = numbers.split(' ')

    current_cloud = 0
    jump_counter = 0

    while can_jump(2,arr,current_cloud) or can_jump(1,arr,current_cloud):
        if can_jump(2,arr,current_cloud):
            if arr[current_cloud + 2] == '0':
                    current_cloud += 2
                    jump_counter+=1
            else:
                current_cloud += 1
                jump_counter+=1
        else:
            current_cloud += 1
            jump_counter+=1

    print(jump_counter)
