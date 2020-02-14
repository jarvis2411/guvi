/*
The area of an equilateral triangle is ¼(√3a2) where "a" represents a side of the triangle. 
You are provided with the side "a". Find the area of the equilateral triangle.

Positive TestCase :
    Input-20
    Output-173.21
*/

function fun(x){
    var a=(1.73205080757/4)*(x**2)
    console.log(a.toFixed(2))
}

fun(20)