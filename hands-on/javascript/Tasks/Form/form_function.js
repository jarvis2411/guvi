document.addEventListener('DOMContentLoaded', ()=>{
    document.getElementById('1234').addEventListener('click', addFormData);
});
var formData = [];
var isEdit = false;
var editIndex;
const addFormData = (ev)=>{
    ev.preventDefault();
    if (formData != "")
    {
        document.getElementById('table').remove()
    }
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
        if (isEdit == true)
         {
            formData[editIndex] = data;
            isEdit = false;
          } 
        else {
            formData.push(data);
        }
    document.forms[0].reset();
    console.log(formData)
    var tab = document.getElementById('tab')
    tab.appendChild(buildTable(formData))
    }
function buildTable(data) {
var table = document.createElement("table");
table.setAttribute('id','table')
table.className="table table-bordered table-dark table-striped table-responsive-sm";
var thead = document.createElement("thead");
thead.setAttribute('class','thead-dark')
var tbody = document.createElement("tbody");
var headRow = document.createElement("tr");
["Name","Email","Password","Country","State","Gender","Marital Status","Favorite Places","",""].forEach(function(el) {
var th=document.createElement("th");
th.appendChild(document.createTextNode(el));
headRow.appendChild(th);
});
thead.appendChild(headRow);
table.appendChild(thead);
tbody.innerHTML = ""
data.forEach(function(el,index) {
var tr = document.createElement("tr");
for (var o in el) {  
var td = document.createElement("td");
td.appendChild(document.createTextNode(el[o]))
tr.appendChild(td);
}
var td = document.createElement('td')
var edit = document.createElement('button')
edit.setAttribute('id','edit')
edit.setAttribute('class','btn btn-warning')
edit.setAttribute('onclick','editRow('+index+')')
edit.innerHTML='Edit'
td.appendChild(edit)
tr.appendChild(td)
var td1 = document.createElement('td')
var del = document.createElement('button')
del.setAttribute('id','delete')
del.setAttribute('class','btn btn-danger')
del.setAttribute('onclick','rowdelete('+index+')')
del.innerHTML='Delete'
td1.appendChild(del)
tr.appendChild(td1)
tbody.appendChild(tr);  
index = index + 1
});
table.appendChild(tbody);             
return table;
}  

function rowdelete(index) 
{
        let result = confirm("Are you sure do you want to delete?");
        if (result) 
        {
          document.getElementById("table").remove()
          formData.splice(index, 1);
          document.getElementById("tab").appendChild(buildTable(formData));

        }
}

function editRow(index) {
    let result = confirm("Are you sure do you want to edit?");
    if (result) 
    {
    document.getElementById("name").value = formData[index].Name;
    document.getElementById("email").value = formData[index].Email;
    document.getElementById("pwd").value = formData[index].Password;
    document.getElementById("repwd").value = formData[index].Password;
    document.getElementById("count").value = formData[index].Country;
    document.getElementById("stat").value = formData[index].State;

    document.getElementsByName("gender").forEach(function(genderObj) {
      if (genderObj.value == formData[index].Gender) {
        genderObj.checked = true;
      }
    });

    document.getElementsByName("martialStatus").forEach(function(msObj) {
      if (msObj.value == formData[index].Maritalstatus) {
        msObj.checked = true;
      }
    });
    isEdit = true;
    editIndex = index;
  }
}