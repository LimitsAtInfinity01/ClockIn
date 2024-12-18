let body = document.getElementsByTagName('tbody')[0];
let rows = body.getElementsByTagName('tr');

data = []
for (let i = 0; i < rows.length; i++){
    data.push(rows[i])
}

data.sort((a, b) => {
    let nameA = a.querySelector('#name').innerText;
    let nameB = b.querySelector('#name').innerText;
    return nameA.localeCompare(nameB);
});


nameHeading = document.querySelector("#nameHeading")
nameHeading.addEventListener("click", function() {
    let body = document.getElementsByTagName('tbody')[0]
    while (body.childElementCount){
        body.removeChild(body.firstElementChild)
    }
    for (let i = 0; i < data.length; i++){
        let row = document.createElement('tr');

        let nameCell = document.createElement('td')
        nameCell.classList.add('td-main')
        nameCell.id = "name";
        nameCell.innerText = data[i].querySelector('#name').innerText;

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
})