/*
You are given with a number A. i.e. the temperature in Celcius. Write a program to convert this into Fahrenheit. 

Positive TestCase :
    Input-32
    Output-89.6
*/

function fun(x){
  var a=(x*(9/5))+32
  var c=a.toFixed(2)
  console.log(c)
}

fun(32)