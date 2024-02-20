#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./101-starwars_characters.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error.message);
  } else if (response.statusCode === 200) {
    const movie = JSON.parse(body);
    const characterUrls = movie.characters;

    function fetchCharacter (index) {
      if (index < characterUrls.length) {
        const characterUrl = characterUrls[index];
        request(characterUrl, (charError, charResponse, charBody) => {
          if (charError) {
            console.error(charError.message);
          } else if (charResponse.statusCode === 200) {
            const character = JSON.parse(charBody);
            console.log(character.name);
            fetchCharacter(index + 1);
          } else {
            console.error(`Failed to retrieve character data. Status code: ${charResponse.statusCode}`);
          }
        });
      }
    }

    fetchCharacter(0);
  } else {
    console.error(`Failed to retrieve movie data. Status code: ${response.statusCode}`);
  }
});
