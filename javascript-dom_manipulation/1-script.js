const header = document.querySelector('header');
const redHeader = document.querySelector('#red_header');

function turnHeaderRed() {
  header.style.color = '#FF0000';
}

redHeader.addEventListener('click', turnHeaderRed);
