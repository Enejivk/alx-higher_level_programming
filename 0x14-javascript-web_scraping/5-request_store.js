#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const path = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    saveContent(body);
  }
});

const saveContent = (body) => {
  fs.writeFile(path, body, (err) => {
    if (err) throw err;
  });
};
