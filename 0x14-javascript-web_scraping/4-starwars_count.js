#!/usr/bin/node
const request = require('request');
let count = 0;
request(process.argv[2], function (error, response) {
  if (!error) {
    for (const film of JSON.parse(response.body).results) {
      for (const figure of film.characters) {
        count = (figure.includes('18')) ? count + 1 : count;
      }
    }
    console.log(count);
  } else {
    console.log(error);
  }
});
