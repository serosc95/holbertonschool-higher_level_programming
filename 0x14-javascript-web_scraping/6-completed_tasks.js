#!/usr/bin/node
const request = require('request');
const obj = {};
request(process.argv[2], function (error, response) {
  if (!error) {
    for (const index of JSON.parse(response.body)) {
      if (index.completed === true) {
        obj[index.userId] = (!obj[index.userId]) ? 1 : obj[index.userId] + 1;
      }
    }
  }
  console.log(obj);
});
