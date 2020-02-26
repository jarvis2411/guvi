var count = 1;
var click = 0
var X = [0,0,0,0,0,0,0,0,0]
function game(x)
{
    var id = x
    var tableData = document.getElementById(id)
    if(count % 2 == 0)
    { 
        tableData.innerHTML = 'O'
        tableData.setAttribute('class','text-warning text-center font-weight-bold')
        X[x] = 'O'
    }
    else
    {
        tableData.innerHTML = 'X'
        tableData.setAttribute('class','text-danger text-center font-weight-bold')
        X[x] = 'X'
    }
    tableData.setAttribute('style','font-size:3em')
    document.getElementById(x).setAttribute('onclick',false)
    count = count + 1
    click ++
    console.log(X)
    if(click>4)
     checkResult(id)
}

function checkResult(id)
{
    console.log(X)
    if(X[0] === X[1] && X[1] === X[2] && X[0] != 0)
    {
        for(i=0;i<9;i++)
        {
            document.getElementById(i).setAttribute('onclick',false)

        }
        document.getElementById(0).setAttribute('class','bg-success text-center font-weight-bold')
        document.getElementById(1).setAttribute('class','bg-success text-center font-weight-bold')
        document.getElementById(2).setAttribute('class','bg-success text-center font-weight-bold')
        alert(X[0]+' wins')
    }
    else if(X[3] === X[4] && X[4] === X[5] && X[3] != 0)
    {
        for(i=0;i<9;i++)
        {
            document.getElementById(i).setAttribute('onclick',false)
        }
        document.getElementById(3).setAttribute('class','bg-success text-center font-weight-bold')
        document.getElementById(4).setAttribute('class','bg-success text-center font-weight-bold')
        document.getElementById(5).setAttribute('class','bg-success text-center font-weight-bold')
        alert(X[3]+' wins')
    }
    else if(X[6] === X[7] && X[7] === X[8] && X[7] != 0)
    {
        for(i=0;i<9;i++)
        {
            document.getElementById(i).setAttribute('onclick',false)
        }
        document.getElementById(6).setAttribute('class','bg-success text-center font-weight-bold')
        document.getElementById(7).setAttribute('class','bg-success text-center font-weight-bold')
        document.getElementById(8).setAttribute('class','bg-success text-center font-weight-bold')
        alert(X[6]+' wins')
    }
    else if(X[0] === X[3] && X[3] === X[6] && X[0]!= 0)
    {
        for(i=0;i<9;i++)
        {
            document.getElementById(i).setAttribute('onclick',false)
        }
        document.getElementById(0).setAttribute('class','bg-success text-center font-weight-bold')
        document.getElementById(3).setAttribute('class','bg-success text-center font-weight-bold')
        document.getElementById(6).setAttribute('class','bg-success text-center font-weight-bold')
        alert(X[0]+' wins')
    }
    else if(X[1] === X[4] && X[4] === X[7] && X[1] !=0)
    {
        for(i=0;i<9;i++)
        {
            document.getElementById(i).setAttribute('onclick',false)
        }
        document.getElementById(1).setAttribute('class','bg-success text-center font-weight-bold')
        document.getElementById(4).setAttribute('class','bg-success text-center font-weight-bold')
        document.getElementById(7).setAttribute('class','bg-success text-center font-weight-bold')
        alert(X[1]+' wins')
    }
    else if(X[2] === X[5] && X[5] === X[8] && X[2] != 0)
    {
        for(i=0;i<9;i++)
        {
            document.getElementById(i).setAttribute('onclick',false)
        }
        document.getElementById(2).setAttribute('class','bg-success text-center font-weight-bold')
        document.getElementById(5).setAttribute('class','bg-success text-center font-weight-bold')
        document.getElementById(8).setAttribute('class','bg-success text-center font-weight-bold')
        alert(X[2]+' wins')
    }
    else if(X[0] === X[4] && X[4] === X[8] && X[0] != 0)
    {
        for(i=0;i<9;i++)
        {
            document.getElementById(i).setAttribute('onclick',false)
        }
        document.getElementById(0).setAttribute('class','bg-success text-center font-weight-bold')
        document.getElementById(4).setAttribute('class','bg-success text-center font-weight-bold')
        document.getElementById(8).setAttribute('class','bg-success text-center font-weight-bold')
        alert(X[0]+' wins')
    }
    else if(X[2] === X[4] && X[4] === X[6] && X[2] != 0)
    {
        for(i=0;i<9;i++)
        {
            document.getElementById(i).setAttribute('onclick',false)
        }
        document.getElementById(2).setAttribute('class','bg-success text-center font-weight-bold')
        document.getElementById(4).setAttribute('class','bg-success text-center font-weight-bold')
        document.getElementById(6).setAttribute('class','bg-success text-center font-weight-bold')
        alert(X[2]+' wins')
    }
    else if(click == 9)
    {   
        for(j=0;j<9;j++)
        {
            document.getElementById(j).setAttribute('class','bg-info text-center font-weight-bold')
        }
        alert("Match is draw")
    }

}