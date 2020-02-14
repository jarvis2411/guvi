/*
You are provided with two numbers. Find and print the smaller number.

Positive TestCase :
    Input-23 12
    Output-12
*/

function fun(x){
    var a=x.split(" ")
    if (a[0]>a[1]){
      console.log(a[1])
    }
    else{
      console.log(a[0])
    }
}

fun("23 12")