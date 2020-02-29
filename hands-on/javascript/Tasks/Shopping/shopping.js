var varientId = 0
var formId = 0
var dataId = 0
var varientTypes = []
var shopping = {}
var varients = []
var varientty = []
var varientDetails = []

function getVarients() {
    varientId++
    formId++
    dataId++
    var buttonDiv = document.getElementById('buttonDiv')
    addVarient()
    if (varientId == 1) {
        var mainDiv = document.getElementById('mainDiv')

        var confirmDiv = document.createElement('div')
        mainDiv.appendChild(confirmDiv)

        var confirmButton = document.createElement('button')
        confirmButton.setAttribute('type', 'button')
        confirmButton.setAttribute('class', 'btn btn-danger')
        confirmButton.setAttribute('id', 'confirmVarients')
        confirmButton.setAttribute('onclick', 'getValues()')
        confirmButton.innerHTML = 'Confirm varients'
        confirmDiv.appendChild(confirmButton)
    }
}

function getValues() {
    document.getElementById('confirmVarients').disabled = true
    document.getElementById('addVarients').disabled = true
    

    shopping['productName'] = document.getElementById('title').value
    shopping['basePrice'] = document.getElementById('price').value

    for (i = 1; i <= formId; i++) {
        varientD = document.getElementById('dataId'+i+'').value
        varientD = varientD.split(',')
        varientType = document.getElementById('varientId'+i+'').value
        varientTypes.push(varientType)
        varient = {
            type: varientType,
            values: varientD
        }
        varients.push(varient)
        displayVarients(varientD)
    }
    shopping['varients'] = varients
    console.log(shopping)
    chechVarients(varientty)
    updateVarients(varientty)
}

function addVarient() {
    var div = document.getElementById('buttonDiv')

    var formgroup = document.createElement('div')
    formgroup.setAttribute('class', 'form-group')
    div.appendChild(formgroup)

    var rowDiv = document.createElement('div')
    rowDiv.setAttribute('class', 'row')
    formgroup.appendChild(rowDiv)

    for (i = 0; i < 2; i++) {
        var colDiv = document.createElement('div')
        rowDiv.appendChild(colDiv)
        var input = document.createElement('input')
        input.setAttribute('type', 'text')
        input.setAttribute('class', 'form-control')
        if (i == 0) {
            colDiv.setAttribute('class', 'col-sm-4')
            input.setAttribute('id', 'varientId'+varientId+'')
            input.setAttribute('placeholder', 'Enter varient type')

        }
        else {
            colDiv.setAttribute('class', 'col-sm-8')
            input.setAttribute('id', 'dataId'+dataId+'')
            input.setAttribute('placeholder', 'Enter the types of the varient')
        }
        colDiv.appendChild(input)
    }
}


function displayVarients(d) {
    len = varientty.length
    if (len > 0) {
        arr = []
        for (k = 0; k < len; k++) {
            for (l = 0; l < d.length; l++) {
                arr.push(varientty[k] + "/" + d[l])
            }
        }
        varientty = arr
    }
    else {
        varientty = d
    }
}

function chechVarients(g) {
    var mainDiv = document.getElementById('mainDiv')
    for (y = 0; y < g.length; y++) {
        ty = g[y].toUpperCase()

        var div = document.createElement('div')
        mainDiv.appendChild(div)

        var formgroup = document.createElement('div')
        formgroup.setAttribute('class', 'form-group')
        div.appendChild(formgroup)

        var label = document.createElement('label')
        label.setAttribute('for', ty)
        label.innerHTML = ty
        formgroup.appendChild(label)


        var input = document.createElement('input')
        input.setAttribute('type', 'text')
        input.setAttribute('class', 'form-control')
        input.setAttribute('id', 'varient'+y+'')
        input.setAttribute('name',ty)
        input.setAttribute('placeholder', 'Enter the price to be added')
        formgroup.appendChild(input)
    }
    var submitDiv = document.createElement('div')
    mainDiv.appendChild(submitDiv)

    var submitButton = document.createElement('button')
    submitButton.setAttribute('type', 'button')
    submitButton.setAttribute('class', 'btn btn-danger')
    submitButton.setAttribute('id', 'submitVarients')
    submitButton.setAttribute('onclick', 'submit()')
    submitButton.innerHTML = 'Submit varients'
    submitDiv.appendChild(submitButton)
}


function submit()
{
    document.getElementById('submitVarients').disabled = true
    for(o=0;o<varientty.length;o++)
    {
        varientDetails[o]['addOnprice'] = document.getElementById('varient'+i+'').value
    }
    shopping['varientDetails'] = varientDetails
    console.log(shopping)
}

function updateVarients(oop)
{
    for(a=0;a<oop.length;a++)
    {
        asd = oop[a].split('/')
        varientDetail = {}
        for(b=0;b<asd.length;b++)
        {
            vt = varientTypes[b]
            vv = asd[b]
            varientDetail[vt] = vv
        }
        varientDetails.push(varientDetail)
    }
}