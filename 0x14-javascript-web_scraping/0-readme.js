#!/usr/bin/node
const fs = require('fs');

const path = process.argv[2];
fs.readFile(path, 'utf8', (err, data) => {
  if (err) throw err;
  console.log(data);
});
