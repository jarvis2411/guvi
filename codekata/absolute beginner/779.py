'''You are provided with two numbers. Find and print the smaller number.

Input Description:
You are provided with two numbers as input.

Output Description:
Print the small number out of the two numbers.

Sample Input :
23 1
Sample Output :
1'''
num1,num2 = input().split()
num1,num2 = float(num1),float(num2)
if num1 > num2:
  print(round(num2))
else:
  print(round(num1))