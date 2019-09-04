#!/usr/bin/python3
"""
Reference: https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

Sample Input 0
aba
10

Sample Output 0
7
--------------------------------------------------------------------------------
Sample Input 1
a
1000000000000

Sample Output 1
1000000000000

"""

if __name__ == "__main__":
  s = input()
  n = int(input())

  s_length = len(s)
  a_count = 0

  for char in s:
    if char == 'a':
      a_count+=1

  mod = n % s_length
  quotient = n // s_length

  ans = a_count * quotient

  for char in range(0, mod):
    if s[char] == 'a':
      ans+=1

  print(ans)
