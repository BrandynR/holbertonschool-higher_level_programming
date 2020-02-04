#!/usr/bin/node

if (!process.argv[2] || isNaN(process.argv[2])) { console.log('Missing size'); }
const list = [];
let i = 0;
for (i = 0; i < process.argv[2]; i++) {
  list.push('X');
}
for (i = 0; i < process.argv[2]; i++) {
  console.log(list.join(''));
}
