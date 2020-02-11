class Player{
    players = [ ]
    overSummary = []
    constructor()
    {
        for(var i=0;i<11;i++){
            this.players.push({"Id": i+1,"Score":0,"Balls":0,"Four":0,"Six":0})
        }
    }   
}
class Team extends Player{
    totalScore = 0
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
        return this.totalScore
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

    setScore(i,b)
    {
        var a = this.players
        if((b+1)<=10){
        var f = Math.floor(Math.random() * 7);
        this.setOver(f,i)
        if (f == 0){
            a[b].Score = a[b].Score
            a[b].Balls += 1
            b = b + 1
            
        }
        else if(f == 4){
            a[b].Score = a[b].Score + f
            a[b].Balls += 1
            a[b].Four += 1
            
        }
        else if(f== 6){
            a[b].Score = a[b].Score + f
            a[b].Balls += 1
            a[b].Six +=1
            
        }
        else{
            a[b].Score = a[b].Score + f
            a[b].Balls += 1
            
        }
        return b
    
}}
}


//User Interface function
var team1 = new Team();
var team2 = new Team()
var i = 0
var j = 0
var b = 0
var c = 0
//Team 1 batting
function setscore1(){
i+= 1
if(i<30){
var d = team1.setScore(i,b)
b = d}
else if(i == 30){
    var d = team1.setScore(i,b)
b = d
    var team1Score = team1.teamScore()
    console.log(team1Score)
    document.getElementById("team1").disabled = true;
    document.getElementById("team2").disabled = false;
}
}
//Team 2 Batting function
function setscore2(){
    j+= 1
    if(j<30){
    var e = team2.setScore(j,c)
    c = e
}
else if(j == 30){
    var e = team2.setScore(j,c)
    c = e
    var team2Score = team2.teamScore()
    console.log(team2Score)
    document.getElementById("team2").disabled = true;
    document.getElementById("summary").disabled = false;
}}
//Gives the summary of the match
function summary()
{
    document.write("-----------Team 1 ----------")
    var a = team1.teamSummary()
    document.write("<br>")
    document.write("<br>")
    for(var i= 1;i<=5;i++)
    {
        team1.getOver(i)
    }
    document.write("<br>")
    document.write("-----------Team 2 ----------")
    var b = team2.teamSummary()
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