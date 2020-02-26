function body()
{
    var body = document.getElementById('body');
    //main container division
    var mainDiv = document.createElement('div');
    mainDiv.setAttribute('class','container-fluid');
    body.appendChild(mainDiv);
    //row division
    var rowDiv = document.createElement('div');
    rowDiv.setAttribute('class','row')
    mainDiv.appendChild(rowDiv)
    //form division
    var formDiv = document.createElement('div');
    formDiv.setAttribute('class','col-sm-6')
    rowDiv.appendChild(formDiv)
    var form = document.createElement('form')
    for(i=1;i<10;i++)
    {
        //form group
        var formGroup = document.createElement('div')
        formGroup.setAttribute('class','form-group')
        if(i==1)
        {
            var label = document.createElement('label')
            label.setAttribute('for','name')
            label.innerHTML = 'Name:'
            formGroup.appendChild(label)
            var input = document.createElement('input')
            input.setAttribute('type','name')
            input.setAttribute('class','form-control')
            input.setAttribute('id','name')
            input.setAttribute('placeholder','Enter your name')
            input.required = true
            formGroup.appendChild(input)
        }
        else if(i==2)
        {
            var label = document.createElement('label')
            label.setAttribute('for','email')
            label.innerHTML = 'Email:'
            formGroup.appendChild(label)
            var input = document.createElement('input')
            input.setAttribute('type','email')
            input.setAttribute('class','form-control')
            input.setAttribute('id','email')
            input.setAttribute('placeholder','Enter your Email')
            input.required = true
            formGroup.appendChild(input)
        }
        else if(i==3)
        {
            var label = document.createElement('label')
            label.setAttribute('for','pwd')
            label.innerHTML = 'Password:'
            formGroup.appendChild(label)
            var input = document.createElement('input')
            input.setAttribute('type','password')
            input.setAttribute('class','form-control')
            input.setAttribute('id','pwd')
            input.setAttribute('placeholder','Enter your password')
            input.required = true
            formGroup.appendChild(input)
        }
        else if(i==4)
        {
            var label = document.createElement('label')
            label.setAttribute('for','repwd')
            label.innerHTML = 'Re-type Password:'
            formGroup.appendChild(label)
            var input = document.createElement('input')
            input.setAttribute('type','password')
            input.setAttribute('class','form-control')
            input.setAttribute('id','repwd')
            input.setAttribute('placeholder','Re-type your password')
            input.required = true
            formGroup.appendChild(input)
        }
        else if(i==5)
        {
            var label = document.createElement('label')
            label.setAttribute('for','country')
            label.innerHTML = 'Country:'
            formGroup.appendChild(label)
            var select = document.createElement('select')
            select.setAttribute('name','country')
            select.setAttribute('id','count')
            select.setAttribute('class','custom-select mb-3')
            for(j=1;j<4;j++)
            {
                var option = document.createElement('option')
                if(j==1)
                {
                    option.setAttribute('value','India')
                    option.innerHTML = 'India'                
                }
                else if(j==2)
                {
                    option.setAttribute('value','USA')
                    option.innerHTML =' USA'                    
                }
                else
                {
                    option.setAttribute('value','UK')
                    option.innerHTML = 'UK' 
                }
                select.appendChild(option)
            }
            formGroup.appendChild(select)
        }
        else if(i==6)
        {
            var label = document.createElement('label')
            label.setAttribute('for','state')
            label.innerHTML = 'State:'
            formGroup.appendChild(label)
            var select = document.createElement('select')
            select.setAttribute('name','state')
            select.setAttribute('id','stat')
            select.setAttribute('class','custom-select mb-3')
            for(j=1;j<4;j++)
            {
                var option = document.createElement('option')
                if(j==1)
                {
                    option.setAttribute('value','TamilNadu')
                    option.innerHTML = 'TamilNadu'                
                }
                else if(j==2)
                {
                    option.setAttribute('value','Meghalaya')
                    option.innerHTML ='Meghalaya'                    
                }
                else
                {
                    option.setAttribute('value','Kerala')
                    option.innerHTML = 'Kerala' 
                }
                select.appendChild(option)
            }
            formGroup.appendChild(select)
        }
        else if(i==7)
        {
            var label = document.createElement('label')
            label.setAttribute('for','custom-radio')
            label.innerHTML = 'Gender'
            formGroup.appendChild(label)
            for(k=1;k<4;k++)
            {
                var radioDiv = document.createElement('div')
                radioDiv.setAttribute('class','custom-control custom-radio')
                var inputRadio = document.createElement('input')
                inputRadio.setAttribute('type','radio')                
                inputRadio.setAttribute('class','custom-control-input')
                var gender;
                if(k==1)
                    gender = 'Male'
                else if(k==2)
                    gender = 'Female'
                else if(k==3)
                    gender = 'Others'
                inputRadio.id = gender
                inputRadio.value = gender
                if(gender=='Male')
                    inputRadio.checked = true
                inputRadio.setAttribute('name','gender')
                radioDiv.appendChild(inputRadio)
                var radioLabel = document.createElement('label')
                radioLabel.setAttribute('class','custom-control-label')
                radioLabel.setAttribute('for',gender)
                radioLabel.innerHTML = gender
                radioDiv.appendChild(radioLabel)
                formGroup.appendChild(radioDiv)
            }
        }
        else if(i==8)
        {
            var label = document.createElement('label')
            label.setAttribute('for','custom-radio')
            label.innerHTML = 'Marital Status'
            formGroup.appendChild(label)
            for(l=1;l<3;l++)
            {
                var radioDiv1 = document.createElement('div')
                radioDiv1.setAttribute('class','custom-control custom-radio')
                var inputRadio1 = document.createElement('input')
                inputRadio1.setAttribute('type','radio')                
                inputRadio1.setAttribute('class','custom-control-input')
                var maritalStatus;
                if(l==1)
                    maritalStatus = 'Unmarried'
                else if(l==2)
                    maritalStatus = 'Married'
                inputRadio1.id = maritalStatus
                inputRadio1.value = maritalStatus
                if(maritalStatus=='Unmarried')
                    inputRadio1.checked = true
                inputRadio1.setAttribute('name','maritalStatus')
                radioDiv1.appendChild(inputRadio1)
                var radioLabel1 = document.createElement('label')
                radioLabel1.setAttribute('class','custom-control-label')
                radioLabel1.setAttribute('for',maritalStatus)
                radioLabel1.innerHTML = maritalStatus
                radioDiv1.appendChild(radioLabel1)
                formGroup.appendChild(radioDiv1)
            }
        }
        else if(i==9)
        {
            var label = document.createElement('label')
            label.setAttribute('for','custom-checkbox')
            label.innerHTML = 'Favorite Places:'
            formGroup.appendChild(label)
            for(k=1;k<4;k++)
            {
                var checkDiv = document.createElement('div')
                checkDiv.setAttribute('class','custom-control custom-checkbox mb-3')
                var inputCheck = document.createElement('input')
                inputCheck.setAttribute('type','checkbox')                
                inputCheck.setAttribute('class','custom-control-input')
                var favoritePlaces;
                if(k==1)
                    favoritePlaces = 'Kodaikanal'
                else if(k==2)
                    favoritePlaces = 'Meghalaya'
                else
                    favoritePlaces = 'Ladakh'
                inputCheck.id = favoritePlaces
                inputCheck.value = favoritePlaces
                if(favoritePlaces=='Ladakh')
                    inputCheck.checked = true
                inputCheck.setAttribute('name','favoritePlaces')
                checkDiv.appendChild(inputCheck)
                var checkLabel = document.createElement('label')
                checkLabel.setAttribute('class','custom-control-label')
                checkLabel.setAttribute('for',favoritePlaces)
                checkLabel.innerHTML = favoritePlaces
                checkDiv.appendChild(checkLabel)
                formGroup.appendChild(checkDiv)
            }
        }
        form.appendChild(formGroup)
    }
    var button = document.getElementById('1234')
    button.setAttribute('class','btn btn-primary')
    button.setAttribute('type','submit')
    button.innerHTML = 'Submit'
    form.appendChild(button)
    formDiv.appendChild(form)

    //table division
    var tableDiv = document.createElement('div')
    tableDiv.setAttribute('class','col-sm-6')
    tableDiv.setAttribute('id','tab')
    rowDiv.appendChild(tableDiv)
    mainDiv.appendChild(rowDiv)
    document.getElementById('name').focus()

}

     
