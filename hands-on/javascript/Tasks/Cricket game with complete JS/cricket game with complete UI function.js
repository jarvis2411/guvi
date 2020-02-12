class Player{
    players = [ ]
    overSummary = []
    constructor()
    {
        for(var i=0;i<11;i++){
            this.players.push({"Id": i+1,"Score":0,"Balls":0,"Four":0,"Six":0})
        }
    }
    getPlayer()
    {
        return this.players
    } 
}
class Team extends Player{
    totalScore = 0
    getScore(){
        return this.totalScore
    }
    teamScore()
    {
        var p = this.players
        for(var i=0;i<11;i++){
            this.totalScore += p[i].Score
        }
        return this.totalScore;
    }
    teamSummary()
    {
        var p = this.players
        for(var i=0;i<11;i++)
        {
            document.write("<br>")
            document.write("Player"+p[i].Id,":",p[i].Score, "-",p[i].Balls,"-",p[i].Four,"-",+p[i].Six)
        }
        document.write("<br>")
        document.write("<br>")
        document.write("Team Score:"+this.totalScore)
    }
    
    showOver(){
        console.log(this.overSummary)
    }
    setOver(run,ball)
    {
        if(run == 0){
            run = 'w'
        }
        console.log(run,ball)
        this.overSummary.push({run,ball})
        return this.overSummary
    }
    getOver(x){
        var over = x * 6
        var o = this.overSummary
        var total = []
        for(var i = (over-6);i<over;i++)
        {
            total.push(o[i].run)
        }
        document.write("Over"+x+":",total)
        document.write("<br>")
    }

    setScore(i,b,x)
    {
        var a = this.players
        if((b+1)<=10){
        var f = Math.floor(Math.random() * 7);
        this.setOver(f,i)
        if(x==1)
        var myTable=document.getElementById('table1');
        else
        var myTable=document.getElementById('table2');
        if (f == 0){
            a[b].Score = a[b].Score
            a[b].Balls += 1
            myTable.rows[b+1].cells[1].innerHTML= a[b].Score
            myTable.rows[b+1].cells[2].innerHTML= a[b].Balls
            b = b + 1
        }
        else if(f == 4){
            a[b].Score = a[b].Score + f
            a[b].Balls += 1
            myTable.rows[b+1].cells[1].innerHTML= a[b].Score
            myTable.rows[b+1].cells[2].innerHTML= a[b].Balls
            a[b].Four += 1
            myTable.rows[b+1].cells[3].innerHTML= a[b].Four
        }
        else if(f== 6){
            a[b].Score = a[b].Score + f
            a[b].Balls += 1
            myTable.rows[b+1].cells[1].innerHTML= a[b].Score
            myTable.rows[b+1].cells[2].innerHTML= a[b].Balls
            a[b].Six +=1       
            myTable.rows[b+1].cells[4].innerHTML= a[b].Six
        }
        else{
            a[b].Score = a[b].Score + f
            a[b].Balls += 1  
            myTable.rows[b+1].cells[1].innerHTML= a[b].Score
            myTable.rows[b+1].cells[2].innerHTML= a[b].Balls          
        }    
        return b
    
}}
}
var team1 = new Team()
var team2 = new Team()
var data1 = team1.getPlayer()
var data2 = team2.getPlayer()
var i = 0
var j = 0
var b = 0
var c = 0
//Team 1 batting
function setscore1(){
i+= 1

if(i<30){
    
var d = team1.setScore(i,b,1)
b = d}
else if(i == 30){
    var d = team1.setScore(i,b,1)
b = d
    var team1Score = team1.teamScore()
    alert("Team1 Score is "+team1Score)
    var t = document.getElementById("team1")
    t.disabled = true;
    t.setAttribute('class','btn btn-danger btn-lg btn-block')
    var u = document.getElementById("team2")
    u.disabled = false;
    u.setAttribute('class','btn btn-success btn-lg btn-block')
    alert("Team1 Innings completed \n Start the Team2 Innings")
}
}
//Team 2 Batting function
function setscore2(){
    j+= 1
    if(j<30){
    var e = team2.setScore(j,c,2)
    c = e
}
else if(j == 30){
    var e = team2.setScore(j,c,2)
    c = e
    var team2Score = team2.teamScore()
    alert("Team2 Score is "+team2Score)
    var t = document.getElementById("team2")
    t.disabled = true;
    t.setAttribute('class','btn btn-danger btn-lg btn-block')
    alert("Team2 Innings completed \n Check Result to see the result")
    document.getElementById("result").disabled = false;
}}
//Gives the result of the match
function result(){
    var a = team1.getScore()
    var b = team2.getScore()
    if(a>b){
        alert("------------Team1 wins-------------")
    }
    else if(a<b){
        alert("------------Team2 wins-------------")
    }
    else{
    alert("------------Match Draws-------------")

}
document.getElementById("result").disabled = true;
document.getElementById("summary").disabled = false;
}
//Gives the summary of the match
function summary()
{
    document.write("-----------Team 1 ----------")
    var a = team1.getScore()
    team1.teamSummary()
    document.write("<br>")
    document.write("<br>")
    for(var i= 1;i<=5;i++)
    {
        team1.getOver(i)
    }
    document.write("<br>")
    document.write("-----------Team 2 ----------")
    var b = team2.getScore()
    team2.teamSummary()
    document.write("<br>")
    document.write("<br>")
    for(var i= 1;i<=5;i++)
    {
        team2.getOver(i)
    }
    if(a>b){
        document.write("<br>")
        document.write("------------Team1 wins-------------")
    }
    else if(a<b){
        document.write("<br>")
        document.write("------------Team2 wins-------------")
    }
    else{
    document.write("<br>")
        document.write("------------Match Draws-------------")
}}
function getplayer(x)
{   var d
    if(x==1){
       d =  team1.getPlayer()
    }
    else{
        d = team2.getPlayer()
    }
    return d;
}
//User Interface function
function good(){
    
    var bod = document.getElementById('body');
    //main container division
    var maindiv = document.createElement('div');
    maindiv.setAttribute('class','container-fluid');
    bod.appendChild(maindiv);
    //1st child division with team 1 table and team1 button
    var maindiv1 = document.createElement('div');
    maindiv.appendChild(maindiv1)
    //button 1
    var button1 = document.createElement('button');
    button1.setAttribute('id','team1')
    button1.setAttribute('content','Team1 - Bat')
    button1.setAttribute('type','button')
    button1.setAttribute('class','btn btn-success btn-lg btn-block')
    button1.setAttribute('onclick','setscore1()')
    button1.innerHTML = 'Team1 - Bat';
    maindiv1.appendChild(button1)
    maindiv1.appendChild(buildTable(data1,1))
    //child div2 for Team 2 table and team2 button
    var maindiv2 = document.createElement('div');
    maindiv.appendChild(maindiv2)
    //Team2 button
    var button2 = document.createElement('button');
    button2.setAttribute('id','team2')
    button2.setAttribute('content','Team1 - Bat')
    button2.setAttribute('type','button')
    button2.setAttribute('onclick','setscore2()')
    button2.innerHTML = 'Team2 - Bat';
    button2.setAttribute('class','btn btn-danger btn-lg btn-block')
    maindiv2.appendChild(button2)
    maindiv2.appendChild(buildTable(data2,2))
    //Result button
    var button4 = document.createElement('button');
    button4.setAttribute('id','result')
    button4.setAttribute('content','Team1 - Bat')
    button4.setAttribute('type','button')
    button4.setAttribute('onclick','result()')
    button4.setAttribute('content', 'test content');
    button4.innerHTML = 'Result';
    button4.setAttribute('class','btn btn-primary btn-lg btn-block')
    maindiv.appendChild(button4)
    //Summary button
    var button3 = document.createElement('button');
    button3.setAttribute('id','summary')
    button3.setAttribute('content','Team1 - Bat')
    button3.setAttribute('type','button')
    button3.setAttribute('onclick','summary()')
    button3.setAttribute('content', 'test content');
    button3.innerHTML = 'Match Summary';
    button3.setAttribute('class','btn btn-primary btn-lg btn-block')
    maindiv.appendChild(button3)
    document.getElementById("team2").disabled = true;
    document.getElementById("summary").disabled = true;
    document.getElementById("result").disabled = true;
    alert("Start the Innings with Team1")

}
function buildTable(data,x) {
    var table = document.createElement("table");
    table.className="table table-bordered table-dark table-striped table-responsive-sm";
    if(x==1)
    table.id="table1";
    else
    table.id="table2"
    var thead = document.createElement("thead");
    thead.setAttribute('class','thead-dark')
    var tbody = document.createElement("tbody");
    var headRow = document.createElement("tr");
    ["Name","Runs","Balls",'Four(s)','Six(es)'].forEach(function(el) {
      var th=document.createElement("th");
      th.appendChild(document.createTextNode(el));
      headRow.appendChild(th);
    });
    thead.appendChild(headRow);
    table.appendChild(thead); 
    data.forEach(function(el) {
      var tr = document.createElement("tr");
      for (var o in el) {  
        var td = document.createElement("td");
        td.appendChild(document.createTextNode(el[o]))
        tr.appendChild(td);
      }
      tbody.appendChild(tr);  
    });
    table.appendChild(tbody);             
    return table;
    
}

