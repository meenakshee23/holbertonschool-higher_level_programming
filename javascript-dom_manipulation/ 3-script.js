const toggleHeader = document.getElementById('toggle_header');
const header = document.querySelector('header');

toggleHeader.addEventListener('click', () => {
  if (header.className === 'red') {
    header.className = 'green';
  } else {
    header.className = 'red';
  }
});
