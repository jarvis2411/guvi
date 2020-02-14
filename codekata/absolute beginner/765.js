/*You are given a number A in Kilometers. Convert this into B: Meters and C: Centi-Metres.

Input Description:
A number "A" representing some distance in kilometer is provided to you as the input.

Output Description:
Convert and print this value in meters and centimeters.

Sample Input :
2.00
Sample Output :
2000.00
200000.00*/
const readline = require('readline');

const inp = readline.createInterface({
  input: process.stdin
});

inp.on("line", (data) => {
	fun(data)
});

function fun(x){
  var B = x*1000
  var C = x*100000
  console.log(B.toFixed())
  console.log(C.toFixed())
}