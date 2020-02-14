'''You will be provided with a number. Print the number of days in the month corresponding to that number.

Note: In case the input is February, print 28 days. If the Input is not in valid range print "Error".

Input Description:
The input is in the form of a number.

Output Description:
Find the days in the month corresponding to the input number. Print Error if the input is not in a valid range.

Sample Input :
8
Sample Output :
31
'''
a = [1,3,5,7,8,10,12]
b = [2,4,6,9,11]
month = int(input())
if month in a:
  print(31)
elif month in b:
  print(30)
elif month == 2:
  print(28)
else:
  print('Error')
