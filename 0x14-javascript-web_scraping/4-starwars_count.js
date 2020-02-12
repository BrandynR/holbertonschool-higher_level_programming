#!/usr/bin/node

const request = require('request');
let counter = 0;
const page = process.argv[2];
request(page, function (error, status, body) {
  if (error) {
    console.error(error);
  }
  const listchar = JSON.parse(body);
  for (let i = 0; i < listchar.results.length; i++) {
    for (let j = 0; j < listchar.results[i].characters.length; j++) {
      if (listchar.results[i].characters[j].search('/18/') > 0) {
        counter += 1;
      }
    }
  }
  console.log(counter);
});
