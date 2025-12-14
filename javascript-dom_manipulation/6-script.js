const characterDiv = document.querySelector('#character');

fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
.then(function (response) {
    return response.json();
})
.then(function (data) {
    characterDiv.textContent = data.name;
})
.catch(function (error) {
    console.log('Error:', error);
});
