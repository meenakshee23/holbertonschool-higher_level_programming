const addItemButton = document.getElementById('add_item');
const myList = document.querySelector('.my_list');

addItemButton.addEventListener('click', () => {
  const li = document.createElement('li');
  li.textContent = 'Item';
  myList.appendChild(li);
});
