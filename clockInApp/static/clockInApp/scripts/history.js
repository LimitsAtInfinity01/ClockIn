console.log("Hello");


document.addEventListener('DOMContentLoaded', function(){
    
    let history_div = document.querySelector(".history-form");
    let content = document.querySelector('.history-content');

    let form = document.querySelector('.form-history');

    let submited = false

    form.addEventListener('submit', function(event){
        event.preventDefault();
        history_div.style.display = 'none';
        content.style.display = 'block';
        submited = true
    })

});



