#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) throw error;
  const json = JSON.parse(body);
  countTask(json);
});

const countTask = (content) => {
  const obj = {};
  for (let i = 1; i <= 10; i++) {
    let count = 0;
    for (const task of content) {
      if (task.userId === i && task.completed === true) {
        count += 1;
      }
      obj[i] = count;
    }
  }
  printing(obj);
};

function printing (obj) {
  console.log(obj);
}
