'''You are given the coefficients of a quadratic equation in order A, B & C.

Where A is the coefficient of X2,  B is the coefficient of X and C is the constant term in the most simplified form.

Example: For  X2 + 5X + 6 = 0, you are given the input as: 1 5 6.

Write a program to find all of the roots of the quadratic.

Note: The output should be up to 2nd decimal place (round off if needed) and in case of a recurring decimal use braces i.e. for eg: 0.33333..... => 0.33.

Note: Use Shri Dharacharya's Method to solve i.e. X = {-b + √(b² - 4ac) } / 2a & {-b-√(b² -4ac)} / 2a

Input Description:
Three numbers corresponding to the coefficients of x(squared), x and constant are given as an input in that particular order

Output Description:
Print the two values of X after rounding off to 2 decimal places if required.

Sample Input :
1 5 6
Sample Output :
-2.00
-3.00
'''
import math
def check_recurrence(val):
    s=str(val).split(".") 
    if(s[0]==s[1]):
        st="("+s+")"
        return float(st)
    return val

def cal_roots(a,b,c,r):
    r1=((-b)+r)/(2*a)
    r2=((-b)-r)/(2*a)
    if(len(str(r1).split("."))>2):
        r1=round(r1,2)
    if(len(str(r2).split("."))>2):
        r2=round(r2,2)
    r1=check_recurrence(r1)
    r2=check_recurrence(r2)
    print("{:.2f}".format(r1))
    print("{:.2f}".format(r2))
    
def root_value(a,b,c):
    r=math.sqrt((b**2)-(4*a*c))
    cal_roots(a,b,c,r)


input_string=input()
input_list=input_string.split()
a=float(input_list[0])
b=float(input_list[1])
c=float(input_list[2])
root_value(a,b,c)