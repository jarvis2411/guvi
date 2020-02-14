/*
You will be provided with a number. 
Print the number of days in the month corresponding to that number.

Positive TestCase :
	Input-12
    Output-31
    
Negative TestCase :
	Input-13
    Output-Error
*/

function fun(x){
  if (x<=12 && x>0){
  	var a=[31,28,31,30,31,30,31,31,30,31,30,31];
  	console.log(a[x-1])
  }
  else{
    console.log("Error") 
  }
}

fun(8)
