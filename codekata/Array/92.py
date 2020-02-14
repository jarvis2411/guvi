'''/*
Given 2 numbers N,K followed by a sorted array of N elements, search and tell if an element K is present in the array.print 'yes' if element is present otherwise print 'no'.
Input Size : 1 <= N <= 1000000000000000(Do it in logN time complexity)
Sample Testcase :
INPUT
3 2
2 3 7
OUTPUT
Yes
*/
'''
N,K = input().split()
array = input().split()
if K in array:
  print("yes")
else:
  print('no')