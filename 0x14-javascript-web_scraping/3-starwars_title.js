#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films';

const final = `${url}/${process.argv[2]}`;

request(final, (error, response) => {
  if (error) {
    console.log(error);
  } else {
    const json = JSON.parse(response.body);
    console.log(json.title);
  }
});
