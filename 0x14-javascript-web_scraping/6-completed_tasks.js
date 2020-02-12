#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let dict = {};

request.get(url, (error, response, body) => {
  if (error) console.log(error);
  else {
    for (const key in JSON.parse(body)) {
      let uid = JSON.parse(body)[key]['userId'];
      if (uid && JSON.parse(body)[key]['completed'] === true) {
        if (dict[uid] === undefined) {
          dict[uid] = 1;
        } else {
          dict[uid] += 1;
        }
      }
    }
  }
  console.log(dict);
});
