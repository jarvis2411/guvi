
"use strict";
function hoist(){
console.log(a,b);
a=10;
var b=20;
console.log(a,b);
}
hoist()
