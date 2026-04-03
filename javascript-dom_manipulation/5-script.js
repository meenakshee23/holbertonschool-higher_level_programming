const updateButton = document.getElementById('update_header');

const mainHeader = document.querySelector('h1'); 

updateButton.addEventListener('click', function() {

    mainHeader.textContent = "New Header!!!";
});
