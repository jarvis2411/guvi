/*
You are provided with a number check whether its odd or even. 

Positive TestCase :
    Input-11
    Output-Odd
*/

function fun(x){
    var a=Math.floor(x)
    if (a==0){
      console.log("Zero")
    }
    else{
        if (a%2==0){
        console.log("Even")
        }
        else{
            console.log("Odd")
        }
    }
}

fun(11)