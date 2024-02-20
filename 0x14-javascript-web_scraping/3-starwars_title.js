#!/usr/bin/node
const axios = require('axios');

if (process.argv.length !== 3) {
  console.error('Usage: ./3-starwars_title.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

axios.get(apiUrl)
  .then(response => {
    console.log(response.data.title);
  })
  .catch(error => {
    console.error(error.message);
  });
