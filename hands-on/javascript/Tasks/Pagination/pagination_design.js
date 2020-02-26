function demo()
{
    var body = document.getElementById('body');
    //main container division
    var mainDiv = document.createElement('div');
    mainDiv.setAttribute('class','container-fluid');
    body.appendChild(mainDiv);
    //table division
    var tableDiv = document.createElement('div');
    mainDiv.appendChild(tableDiv);
    //table building to store the data
    tableDiv.appendChild(buildTable(json))
    //pagination division
    var pageDiv = document.createElement('div')
    var page = document.createElement('ul')
    page.setAttribute('class','pagination pagination-lg justify-content-end')
    //page creation
    for(i=0;i<20;i++)
    {
        var id = i+1
        var list = document.createElement('li')
        list.setAttribute('class','page-item')
        list.setAttribute('id',i)
        var link = document.createElement('a')
        link.setAttribute('class','page-link')
        link.setAttribute('onclick','qdemo('+i+')')
        link.innerHTML = id
        list.appendChild(link)
        page.appendChild(list)
    }
    pageDiv.appendChild(page)
    mainDiv.appendChild(pageDiv)
    var t = document.getElementById('0')
    t.setAttribute('class','page-item active')
}

//table creation
function buildTable(data) {
var table = document.createElement("table");
table.setAttribute('id','table')
table.className="table table-bordered table-dark table-striped table-responsive-sm";
var thead = document.createElement("thead");
thead.setAttribute('class','thead-dark')
var tbody = document.createElement("tbody");
var headRow = document.createElement("tr");
["Id","Name","Email"].forEach(function(el) {
var th=document.createElement("th");
th.appendChild(document.createTextNode(el));
headRow.appendChild(th);
});
thead.appendChild(headRow);
table.appendChild(thead);
var data1= []
for(i=0;i<5;i++)
{
data1.push(data[i])
} 
data1.forEach(function(el) {
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


//different page
function qdemo(x)
{
     //var act = document.getElementsByClassName('page-item active')
     //act.setAttribute('class','page-item')
    var t = document.getElementById(page)
    t.setAttribute('class','page-item')
    var u = document.getElementById(x)
    u.setAttribute('class','page-item active')
     var table = document.getElementById("table")
    var row = 1
    for(i=(x*5);i<((x*5)+5);i++)
    {
        table.rows[row].cells[0].innerHTML = json[i].id
        table.rows[row].cells[1].innerHTML = json[i].name
        table.rows[row].cells[2].innerHTML = json[i].email
        row = row + 1
    }
    page = x
}