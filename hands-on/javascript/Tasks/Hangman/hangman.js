const a = ['guvi', 'water', 'board', 'geeks']
var word = a[Math.floor(Math.random() * a.length)]
word = word.toUpperCase()
var word_length=word.length;
var word1 = []
var n = 12
var d = 0
var str="";
    console.log(word)
	for(i=0;i<word_length;i++){
		var str=str+" _";
    }
function good()
{
    var body = document.getElementById("body")
    var div = document.createElement("div")
    div.setAttribute("class",'container-fluid')
    body.appendChild(div)
    var heading = document.createElement('h1')
    heading.setAttribute('class','text-success text-center')
    heading.innerHTML = "Guess the word!!!"
    div.appendChild(heading) 
	alert("Let's play Hangman Game");
    var h=document.createElement("h3");
    h.setAttribute('class','text-primary')
	h.textContent= str;
    div.appendChild(h);
    var div1 = document.createElement('div')
    div1.setAttribute('class','btn-group')
    div.appendChild(div1)
    for(i=65;i<91;i++)
    {
        var b5 = document.createElement('button');
        var t = String.fromCharCode( i )
        b5.setAttribute('id',t)
        b5.setAttribute('type','button')
        b5.setAttribute('class','btn btn-primary')
        b5.setAttribute('onclick','check(id)')
        b5.innerHTML = t;
        div1.appendChild(b5)
    }
}
function check(id){
    while(n > 0)
    {
        if(d < word_length)
        {
            
            if(word.includes(id))
            {
                var y = document.getElementById(id)
                document.getElementById(id).disabled = true;
                y.setAttribute('class','btn btn-success')
                alert("You have chosen correct letter "+id)
                console.log(id)
                n = n - 1
                alert("You have "+n+" chances")
                for(var i=0;i<word_length;i++)
                {
                    if(word[i] == id)
                    {
                        word1[i] = id
                        d = d + 1
                    }
                }
                if(d == word_length)
                {
                    if(n>0)
                    {
                        alert("You Won!!!")
                        alert("The word is",word1)
                        for(var i =65;i<91;i++)
                        {
                            var t = String.fromCharCode( i )
                            document.getElementById(t).disabled = true;
                       }
                    }
                }
                break
            }
            else
            {
                var y = document.getElementById(id)
                document.getElementById(id).disabled = true;
                y.setAttribute('class','btn btn-danger')
                alert("You have chosen wrong letter "+id)
                console.log(id)
                n = n - 1 
                alert("You have "+ n +" chances")
                console.log(n)
                break
            }
        }
           
    }  
    if (n == 0)
    {
       var a = 0
       alert("You Lost!!!")
    }
}


