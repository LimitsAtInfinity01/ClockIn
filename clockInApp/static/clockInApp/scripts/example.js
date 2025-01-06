document.addEventListener('DOMContentLoaded', function () {
    const button = document.querySelector('#fetchData');
    const responseDiv = document.querySelector('#response');

    button.addEventListener('click', function () {
        fetch('/example-view/') // Replace with the correct URL for your Django view
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                // Clear previous response
                responseDiv.innerHTML = '';

                // Display the JSON data
                const name = document.createElement('p');
                name.textContent = `Name: ${data.name}`;
                const type = document.createElement('p');
                type.textContent = `Type: ${data.type}`;
                responseDiv.appendChild(name);
                responseDiv.appendChild(type);
            })
            .catch(error => {
                responseDiv.innerHTML = `<p class="error">Error: ${error.message}</p>`;
            });
    });
});