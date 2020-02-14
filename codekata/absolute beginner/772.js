/*
Let "A"  be a string. Remove all the whitespaces and find it's length.

Positive TestCase :
    Input-Lorem Ipsum
    Output-10
*/

function fun(x){
  var a=''
  for(i in x){
    if (x[i]==' '){
      continue
    }
    else{
      var a=a+x[i]
    }
  }
  console.log(a.length)
}

var b="Lorsem Ipsum"
fun(b)