#!/usr/bin/node
const request = require('request');
const obj = {};
let count = 0;
request(process.argv[2], function (error, response) {
  if (!error) {
    for (const index of JSON.parse(response.body)) {
      count = (obj[index.userId]) ? obj[index.userId] : 0;
      obj[index.userId] = (index.completed) ? ++count : count;
    }
  }
  console.log(obj);
});
