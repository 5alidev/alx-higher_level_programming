#!/usr/bin/node

const request = require('request');
const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request(url, (err, res, body) => {
  if (err) {
    console.error(err);
  }

  const films = JSON.parse(body);
  const characters = films.characters;

  const characterPromises = characters.map(charUrl => {
    return new Promise((resolve, reject) => {
      request(charUrl, (error, response, bd) => {
        if (error) {
          reject(error);
        } else {
          const character = JSON.parse(bd);
          resolve(character.name);
        }
      });
    });
  });
  Promise.all(characterPromises)
    .then(names => {
      names.forEach(name => console.log(name));
    })
    .catch(error => console.error(error));
});
