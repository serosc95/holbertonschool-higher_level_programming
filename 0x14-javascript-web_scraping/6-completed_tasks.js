#!/usr/bin/node
const request = require('request');
const obj = {};
const url = `${process.argv[2]}?completed=true`;
request(url, function (error, response) {
  if (!error) {
    for (const index of JSON.parse(response.body)) {
      obj[index.userId] = (!obj[index.userId]) ? 1 : obj[index.userId] + 1;
    }
  }
  console.log(obj);
});
