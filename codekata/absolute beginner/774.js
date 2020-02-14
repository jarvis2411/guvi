/*
Print the First 3 multiples of the given number "N".(N is a positive integer)

Positive TestCase :
    Input-2
    Output-2 4 6
*/

function fun(x){
    var a=''
    for (i=1; i<=3; i++){
      if (i<3){
      var a=a+(i*x)+' '
      }
      else{
        var a=a+(i*x)
        } 
    }
    console.log(a)
}


fun(2)