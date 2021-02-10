#!/usr/bin/node
const request = require('request');
let count = 0;
const character = 'https://swapi-api.hbtn.io/api/people/18/';
request(process.argv[2], function (error, response) {
  if (!error) {
    for (const film of JSON.parse(response.body).results) {
      for (const figures of film.characters) {
        count = (figures === character) ? count + 1 : count;
      }
    }
    console.log(count);
  } else {
    console.log(error);
  }
});
