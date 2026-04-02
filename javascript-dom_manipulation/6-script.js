const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
const characterEl = document.getElementById('character');

async function fetchCharacter() {
  try {
    const response = await fetch(url);
    const data = await response.json();
    characterEl.textContent = data.name;
  } catch (error) {
    console.error('Error fetching character:', error);
  }
}

fetchCharacter();