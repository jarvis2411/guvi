
class calculator{
    setNumber(){
        var num1 = parseInt(prompt('Enter number 1:'));
        var num2 = parseInt(prompt('Enter number 2:'));
        this.num1 = num1;
        this.num2 = num2;
    }
    addition(){
        return this.num1+this.num2;
    }
    subraction(){
        return this.num1-this.num2;
    }
    nultiplication(){
        return this.num1*this.num2;
    }
    division(){
        return this.num1/this.num2;
    }
}
var calc = new calculator();
while(true){
var input = prompt('1.Addition 2.Subraction 3.Multiplication 4.Division 5.Exit');
if(input == 1 || input == "Addition" || input == "Add"){
    calc.setNumber();
    var sum = calc.addition();
    alert(sum);
}
else if(input == 2 || input == "Subtraction" || input == "Sub"){
    calc.setNumber();
    var sub = calc.subraction();
    alert(sub);
}
else if(input == 3 || input == "Multiplication" || input == "Mul"){
    calc.setNumber();
    var mul = calc.nultiplication();
    alert(mul);
}
else if(input == 4 || input == "Division" || input == "Div"){
    calc.setNumber();
    var div = calc.divsion();
    alert(div);}
else if(input == 5 || input == "Exit"){
    break
}
else{
    alert("Enter valid option")
}
}