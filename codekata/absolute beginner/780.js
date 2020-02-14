/*
You are given with Principle amount($), Interest Rate(%) and Time (years) in that order. Find Simple Interest.

Positive TestCase :
    Input-1000 2 5
    Output-100.00
*/

function fun(x){
    var a=x.split(" ")
    var d=((a[0]*a[1]*a[2])/100)
    console.log(d.toFixed(2))
}

var b=1000 2 5
fun(b)