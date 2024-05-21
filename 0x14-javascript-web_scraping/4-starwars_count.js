#!/usr/bin/node

const request = require('request');
const starWarsUrl = process.argv[2];
let countWedgeAntilles = 0;

request(starWarsUrl, (err, res, body) => {
  if (err) {
    console.error(err);
  }
  const films = JSON.parse(body).results;
  for (let i = 0; i < films.length; i++) {
    for (let j = 0; j < films[i].characters.length; j++) {
      if (films[i].characters[j].includes('people/18/')) {
        countWedgeAntilles++;
      }
    }
  }
  console.log(countWedgeAntilles);
});
