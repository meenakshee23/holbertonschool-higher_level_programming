document.addEventListener('DOMContentLoaded', function () {
  const helloDiv = document.querySelector('#hello');

  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      helloDiv.textContent = data.hello;
    })
    .catch(function (error) {
      console.log('Error:', error);
    });
});
