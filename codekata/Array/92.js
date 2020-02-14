/*
Given 2 numbers N,K followed by a sorted array of N elements, search and tell if an element K is present in the array.print 'yes' if element is present otherwise print 'no'.
Input Size : 1 <= N <= 1000000000000000(Do it in logN time complexity)
Sample Testcase :
INPUT
3 2
2 3 7
OUTPUT
Yes
*/
const readline = require('readline');

const inp = readline.createInterface({
  input: process.stdin
});

const userInput = [];

inp.on("line", (data) => {
	userInput.push(data);
});

inp.on("close", () => {
	var t = []
    for(i=0;i<userInput.length;i++){
    var a=userInput[i].split(" ")
    t.push(a)    
    }
    fun(t)
});

function fun(x){
    
    var z = x[0][1]
    var y = x[0][0]
    var  w = 0
    for(var i=0;i<y;i++){
        if(z == x[1][i]){
            w = 1
        }
    }
    if(w==1)
    {
        console.log("yes")
    }
    else{
        console.log("no")
    }
}
