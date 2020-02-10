var Httpreq = new XMLHttpRequest(); // a new request
    Httpreq.open("GET",'https://restcountries.eu/rest/v2/all',false);
    Httpreq.send(null);
    var x = Httpreq.responseText;    
    json_obj = JSON.parse(x);


function load(){
    var bod = document.getElementById('body');
    var maindiv = document.createElement('div');
    maindiv.setAttribute('class','container-fluid');
    bod.appendChild(maindiv);
    var row1 = document.createElement('div');
    row1.setAttribute('class','right');
    row1.setAttribute('id','right');
    maindiv.appendChild(row1)
    for(i=0;i<5;i++){
    console.log(i)
    var row = document.createElement('div');
    row.setAttribute('class','row');
    row.setAttribute('id','row')
    maindiv.appendChild(row);
    k = 4 * i
    l = k + 4
    for(j=k;j<l;j++){
        var div = document.getElementById('row');
        var card = document.createElement('div');
        card.setAttribute('class','col-md-3 col-sm-2');
        var image = document.createElement('img');
        image.setAttribute('src',json_obj[j].flag);
        image.setAttribute('class','img-responsive img-thumbnail rounded-circle')
        image.setAttribute('id',j);
        image.setAttribute('width','300px');
        image.setAttribute('height','300px');
        image.setAttribute('onclick','info(id)');
        card.appendChild(image);
        div.appendChild(card); 
        }
    
    }row.appendChild(div);}

    function info(x){
                    

            var countryName=json_obj[x].name;
            var alphaCode=json_obj[x].alpha2Code;
            var capital=json_obj[x].capital;
            var region=json_obj[x].region;
            var border='';
            var borderLength=(json_obj[x]['borders']).length;

            if (borderLength===0){
                var border= border + 'It is an island surrounded by water';
            }
            else{
                for (i=0; i<(json_obj[x]['borders']).length; i++){
                    var border=(border + (json_obj[x]['borders'][i]));
                    var border=border+' ';
                }
            }   
            var details=('Country : ' + countryName + '<br>' + 'Alpha Code : ' + alphaCode + '<br>' + 'Region : ' + region + '<br>' + 'Border : ' + border);
            console.log(details)
            document.getElementById('right').innerHTML=details;
    }

        