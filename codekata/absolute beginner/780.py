'''You are given with Principle amount($), Interest Rate(%) and Time (years) in that order. Find Simple Interest.

Print the output up to two decimal places (Round-off if necessary).

(S.I. = P*T*R/100)

Input Description:
Three values are given to you as the input. these values correspond to Principle amount, Interest Rate and Time in that particular order.

Output Description:
Find the Simple interest and print it up to two decimal places. Round off if required.

Sample Input :
1000 2 5
Sample Output :
100.00'''
principalAmount,interestRate,time = input().split()
p,i,t = float(principalAmount),float(interestRate),float(time)
simpleInterest = (p*i*t)/100
print(round(simpleInterest,2))