'''
Given 2 numbers N,K print the array after deleting the last K elements.
Input Size : N,K <= 100000
Sample Testcase :
INPUT
5 4
1 2 3 4 5
OUTPUT
1
'''
N,K = input().split()
N,K = int(N),int(K)
a = input().split()
b = []
for i in range(0,N-K):
  b.append(a[i])
print(' '.join(b))