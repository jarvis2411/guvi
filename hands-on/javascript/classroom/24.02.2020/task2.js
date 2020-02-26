var formData = [];
function oo(ev)
{
    ev.preventDefault();
    var gender = function(){
        var ele = document.getElementsByName('gender'); 
            for(i  = 0; i < ele.length; i++) { 
                if(ele[i].checked) 
                    return ele[i].value 
            } 
    }
    var maritalStatus = function()
    {
        var ele = document.getElementsByName('maritalStatus'); 
            for(i = 0; i < ele.length; i++) { 
                if(ele[i].checked) 
                    return ele[i].value 
            } 
    }
    var favoritePlaces = function()
    {
        var array = []
        var ele = document.getElementsByName('favoritePlaces'); 
        for(i = 0; i < ele.length; i++) { 
            if(ele[i].checked) 
                array.push(ele[i].value)
        }
        return array    
    }
    let data = {
        Name: document.getElementById('name').value,
        Email: document.getElementById('email').value,
        Password: document.getElementById('pwd').value,
        Country: document.getElementById('count').value,
        State: document.getElementById('stat').value,
        Gender: gender(),
        Maritalstatus: maritalStatus(),
        FavoritePlaces: favoritePlaces()
        }
    formData.push(data);
    document.forms[0].reset();
    }

console.log(formData)