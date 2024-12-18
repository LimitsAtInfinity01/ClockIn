
main()

function main(){
    // Sort by name
    headingNameCell = document.querySelector("#nameHeading");
    headingNameCell.addEventListener("click", function(){
        let data = getTableData();
        let sortedData = sortData(data, "#name");
        removeBody()
        createBody(sortedData)
    })
    
    headingLastNameCell = document.querySelector("#lastNameHeading");
    headingLastNameCell.addEventListener("click", function(){
        let data = getTableData();
        let sortedData = sortData(data, "#lastName");
        removeBody()
        createBody(sortedData)
    })

    headingWorkedTimeCell = document.querySelector('#workedTimeHeading')
    headingWorkedTimeCell.addEventListener('click', function(){
        let data = getTableData();
        sortedData = sortTimeData(data)
        removeBody()
        rebuildBodyByTime(sortedData)
    })
}


function getTableData(){
    let body = document.getElementsByTagName('tbody')[0];
    let rows = body.getElementsByTagName('tr');
    data = []
    for (let i = 0; i < rows.length; i++){
        data.push(rows[i])
    }
    return data
}

function sortData(data, selector){
    data.sort((a, b) => {
        let nameA = a.querySelector(selector).innerText;
        let nameB = b.querySelector(selector).innerText;
        return nameA.localeCompare(nameB);
    }); 
    return data
}


function removeBody(){
    let body = document.getElementsByTagName('tbody')[0]
    while (body.childElementCount){
        body.removeChild(body.firstElementChild)
    }
}

function createBody(data){
    let body = document.getElementsByTagName('tbody')[0]
    for (let i = 0; i < data.length; i++){
        let row = document.createElement('tr');

        let nameCell = document.createElement('td')
        nameCell.classList.add('td-main')
        nameCell.id = "name";
        nameCell.innerText = data[i].querySelector("#name").innerText;
        
        let lastNameCell = document.createElement('td')
        lastNameCell.classList.add('td-main')
        lastNameCell.id = "lastName"
        lastNameCell.innerText = data[i].querySelector('#lastName').innerText

        let timeInCell = document.createElement('td')
        timeInCell.classList.add('td-main')
        timeInCell.id = "timeIn"
        timeInCell.innerText = data[i].querySelector('#timeIn').innerText

        let timeOutCell = document.createElement('td')
        timeOutCell.classList.add('td-main')
        timeOutCell.id = "timeOut"
        timeOutCell.innerText = data[i].querySelector('#timeOut').innerText

        let workedTimeCell = document.createElement('td')
        workedTimeCell.classList.add('td-main')
        workedTimeCell.id = "workedTime"
        workedTimeCell.innerText = data[i].querySelector('#workedTime').innerText

        row.appendChild(nameCell);
        row.appendChild(lastNameCell);
        row.appendChild(timeInCell);
        row.appendChild(timeOutCell);
        row.appendChild(workedTimeCell);
        body.appendChild(row);
    }
}


// 3:31:01.594319
// H:MM:SS.MS
function sortTimeData(data){
    seconds = []
    newData = []
    for (let i = 0; i < data.length; i++){
        let wholeTime = data[i].querySelector('#workedTime').innerText
        // console.log(wholeTime)
        splitTime = wholeTime.split(':')
        totalSeconds = (parseFloat(splitTime[0]) * 3600) + 
                       (parseFloat(splitTime[1]) * 60) + 
                       (parseFloat(splitTime[2]))
        seconds.push(totalSeconds)
        objectData = {
            totalSeconds: totalSeconds,
            originalData: data[i]
        }
        newData.push(objectData)
    }
    newData.sort((a, b) => a.totalSeconds - b.totalSeconds)
    return newData
}

function rebuildBodyByTime(data){
    let body = document.getElementsByTagName('tbody')[0]
    for (let i = 0; i < data.length; i++){
        console.log(data[i]['originalData'])
        body.appendChild(data[i]['originalData'])
    }
}

