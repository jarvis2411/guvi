/*Given 2 numbers N,K print the array after deleting the last K elements.
Input Size : N,K <= 100000
Sample Testcase :
INPUT
5 4
1 2 3 4 5
OUTPUT
1*/
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
    
    var z = []
    var y = x[0][0] - x[0][1]
    for(var i=0;i<y;i++){
        z.push(x[1][i])
    }
    console.log(...z)
}
