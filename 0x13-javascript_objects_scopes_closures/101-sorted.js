#!/usr/bin/node

const dict = require('./101-data.js').dict;
const retDict = {};
const prev = [];

for (const key in dict) {
  if (prev.indexOf(dict[key])) {
    retDict[dict[key]] = [];
    for (const k in dict) {
      if (dict[k] === dict[key]) {
        retDict[dict[k]].push(k);
      }
    }
  }
  prev.push(key);
}

console.log(retDict);
