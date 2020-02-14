/*
Using the method of looping, write a program to print the table of 9 till N in the format as follows:
(N is input by the user)

Positive TestCase :
    Input-3
    Output-9 18 27

Negative TestCase :
    Input-0
    Output-NULL
*/

function fun(x){
  if (x>0){
    var a="";
    for (i=1; i<=x; i++){
      if (i<x){
    	var a=a+(i*9)+" ";
    	}
      else{
        var a=a+(i*9);
        }
    }
    console.log(a)
  }
  else{
    console.log("NULL")
  }
}

fun(3)