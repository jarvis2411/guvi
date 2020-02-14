'''Let "A"  be a string. Remove all the whitespaces and find it's length.

Input Description:
A string is provide as an input

Output Description:
Remove all the whitespaces and then print the length of the remaining string.

Sample Input :
Lorem Ipsum
Sample Output :
10'''

A = input()
a = 0
for i in range(len(A)):
  if ord(A[i]) == 32:
    a += 1
print(len(A)-a)

