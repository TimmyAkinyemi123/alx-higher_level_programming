#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./starwars_count.js <api_url>');
  process.exit(1);
}

const apiUrl = process.argv[2];
const characterId = 18;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error.message);
  } else if (response.statusCode === 200) {
    const filmsData = JSON.parse(body);
    const count = filmsData.results.reduce((acc, film) => {
      if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
        return acc + 1;
      }
      return acc;
    }, 0);

    console.log(count);
  } else {
    console.error(`Failed to retrieve data. Status code: ${response.statusCode}`);
  }
});
