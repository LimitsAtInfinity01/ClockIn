import { formattedData } from './timeFormating.js'
// import {SortingTable} from './sortTableClass.js'

document.addEventListener('DOMContentLoaded', function() {
    
    const history_div = document.querySelector(".history-form");      // The form container
    const content = document.querySelector(".history-content");       // The content container
    const form = document.querySelector(".form-history");
    const searchBtn = document.querySelector('.search-btn')
    const searchDiv = document.querySelector('.search-div')
    const search_results = document.querySelector('.search-results')

    // Limit table to current week only
    form.addEventListener("submit", function(event){
        event.preventDefault();  // Stop the traditional form submission

        // Gather form data
        let formData = new FormData(form);  
        fetch("/myWorkHistory", {
            method: "POST",
            body: formData,
            headers: {
                "X-CSRFToken": "token"
            }
        })
        .then(response => {

            if (!response.ok) {
                throw new Error("Incorrect password or server error");
            }
            return response.json();  
        })
        .then(entries => {

            const formatedData = entries.map(entry => formattedData(entry))

            history_div.style.display = "none";
            content.style.display = "block"
            
            let table = document.createElement('table')
            let thead = document.createElement('thead')
            let tbody = document.createElement('tbody')

            content.appendChild(table)
            table.appendChild(thead)
            table.appendChild(tbody)
            
            const properties = Object.keys(formatedData[0])
            properties.forEach(property => {
                let heading = document.createElement('th')
                heading.innerText = property
                heading.classList.add("th-main")
                thead.appendChild(heading)
            })

            const values = Object.values(formatedData[0])
            formatedData.forEach(entry => {
                const tr = document.createElement('tr')
                values.forEach((value) => {
                    const td = document.createElement('td')
                    td.textContent = value
                    td.classList.add("td-main")
                    tr.appendChild(td) 
                })
                tbody.appendChild(tr)
            })

            searchDiv.style.display = 'block'
        })
        .catch(error => {
            alert(error.message);
        });
    });

    // Search is to display older days
    searchBtn.addEventListener('click', (event) => {
        const searchBox = document.querySelector('.search-box');
        const searchTerm = searchBox.value;
        
        fetch(`/searchBox-API/?q=${searchTerm}`)
        .then(response => {
            if (!response.ok) {
                throw new Error("Incorrect password or server error");
            }
            return response.json();  
        })
        .then(data => {
            const newData = data.map(entry => formattedData(entry))

            let table = document.createElement('table')
            let thead = document.createElement('thead')
            let tbody = document.createElement('tbody')

            search_results.appendChild(table)
            table.appendChild(thead)
            table.appendChild(tbody)

            // since the headings of the table are always the same
            // but for dynamic use map
            const properties = Object.keys(newData[0])
            properties.forEach(property => {
                let heading = document.createElement('th')
                heading.innerText = property
                heading.classList.add("th-main")
                thead.appendChild(heading)
            })

            const values = Object.values(newData[0])
            newData.forEach(entry => {
                const tr = document.createElement('tr')
                values.forEach((value) => {
                    const td = document.createElement('td')
                    td.textContent = value
                    td.classList.add("td-main")
                    tr.appendChild(td) 
                })
                tbody.appendChild(tr)
            })

            search_results.style.display = 'block'
            console.log(properties)
            console.log(newData)
        })
        .catch(error => {
            console.error(error)
        })
    })
});


// 01-12-2025