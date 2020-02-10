class Team{
    players = [
        {"Id": 1,"Score":0,"Balls":0,"Four":0,"Six":0},
    {"Id": 2,"Score":0,"Balls":0,"Four":0,"Six":0},
    {"Id": 3,"Score":0,"Balls":0,"Four":0,"Six":0},
    {"Id": 4,"Score":0,"Balls":0,"Four":0,"Six":0},
    {"Id": 5,"Score":0,"Balls":0,"Four":0,"Six":0},
    {"Id": 6,"Score":0,"Balls":0,"Four":0,"Six":0},
    {"Id": 7,"Score":0,"Balls":0,"Four":0,"Six":0},
    {"Id": 8,"Score":0,"Balls":0,"Four":0,"Six":0},
    {"Id": 9,"Score":0,"Balls":0,"Four":0,"Six":0},
    {"Id": 10,"Score":0,"Balls":0,"Four":0,"Six":0},
    {"Id": 11,"Score":0,"Balls":0,"Four":0,"Six":0}
    ]
    getScore()
    {
        for(var i=0;i<11;i++)
        {
            var p = this.players
            console.log(p[i].Id,p[i].Score,p[i].Balls);
        }
    }
    getBalls()
    {
        for(var i=0;i<11;i++)
        {
            var p = this.players
            console.log(p[i].Id,p[i].Balls);
        }
    }
    teamScore()
    {
        var p = this.players
        var totalScore = 0
        for(var i=0;i<11;i++){
            totalScore += p[i].Score
        }
        return totalScore;
    }
    teamSummary()
    {
        var p = this.players
        for(var i=0;i<11;i++)
        {
            console.log("Player"+p[i].Id,"Score:"+p[i].Score,"Balls Played:"+p[i].Balls,"Four(s):"+p[i].Four,"Six(es):"+p[i].Six)
        }
    }

}
class Player extends Team{

    setScore()
    {
        var a = this.players
        var b = 0
        for(var i=1;i<=30;i++){
            var f = Math.floor(Math.random() * 7);
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
    }
}
}

var team1 = new Player();
team1.setScore()
var team1Score =  team1.teamScore()
team1.teamSummary()
console.log("Team1 Score:",team1Score)
var team2 = new Player();
team2.setScore()
var team2Score = team2.teamScore()
team2.teamSummary()
console.log("Team2 Score:",team2Score)
if(team1Score > team2Score)
    console.log("Team 1 wins")
else if(team2Score > team1Score)
    console.log("Team 2 wins")
else
    console.log("Match Draws")