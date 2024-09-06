#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

request(`https://swapi-api.hbtn.io/api/films/${movieId}`, function (error, response, body) {
  if (error) throw error;
  const charactersURL = JSON.parse(body).characters;
  printCharactersName(charactersURL, 0);
});
const printCharactersName = (charactersURL, i) => {
  if (i === charactersURL.length) return;
  request(charactersURL[i], function (err, res, body) {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    printCharactersName(charactersURL, i + 1);
  });
};
