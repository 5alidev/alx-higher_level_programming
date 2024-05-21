#!/usr/bin/node

request = require('request');
const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request(url, (err, res, body) => {
  if (err) {
    console.error(err);
  }
  const films = JSON.parse(body);
  const characters = films.characters;

  characters.forEach(char => {
    let charUrl = char;
    request(charUrl, (error, response, bd) => {
      if (error) {
        console.error(error);
      }
      const character = JSON.parse(bd);
      console.log(character.name);
    });
  });
});
