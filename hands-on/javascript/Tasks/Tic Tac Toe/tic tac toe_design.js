function body()
{
    //main division
    var mainDiv = document.createElement('div')
    mainDiv.setAttribute('class','container')
    document.body.appendChild(mainDiv)

    //heading
    var heading = document.createElement('h1')
    heading.setAttribute('class','text-success text-center')
    heading.innerHTML = " TIC TAC TOE"
    mainDiv.appendChild(heading)

    //table  for game
    var id = 0
    var table = document.createElement('table')
    table.setAttribute('class','table table-bordered table-responive-sm table-lg')
    table.setAttribute('style','background-color:#ffa372')
    var tableBody = document.createElement('tbody')
    tableBody.setAttribute('class','text-center')
    for(i=1;i<=3;i++)
    {
        var tableRow = document.createElement('tr')
        tableRow.setAttribute('style','height:100px; width:100px')
        for(j=1;j<=3;j++)
        {
            var tableData = document.createElement('td')
            tableData.id = id
            tableData.setAttribute('onclick','game('+id+')')
            tableData.setAttribute('class','text-center font-weight-bold')
            tableRow.appendChild(tableData)
            id = id + 1
        }
        tableBody.appendChild(tableRow)
    }
    table.appendChild(tableBody)
    mainDiv.appendChild(table)
}