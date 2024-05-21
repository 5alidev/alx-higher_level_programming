#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const completedObj = {};

request(url, (err, res, body) => {
  const todos = JSON.parse(body);
  if (err) {
    console.log(err);
  }
  for (let i = 0; i < todos.length; i++) {
    if (todos[i].completed && completedObj[todos[i].userId] === undefined) {
      completedObj[todos[i].userId] = 1;
    } else if (todos[i].completed) {
      completedObj[todos[i].userId] += 1;
    }
  }
  console.log(completedObj);
});
