#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./6-completed_tasks.js <api_url>');
  process.exit(1);
}

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error.message);
  } else if (response.statusCode === 200) {
    const todos = JSON.parse(body);
    const completedTasksByUser = {};

    todos.forEach((todo) => {
      if (todo.completed) {
        const userId = todo.userId.toString();
        completedTasksByUser[userId] = (completedTasksByUser[userId] || 0) + 1;
      }
    });

    console.log(completedTasksByUser);
  } else {
    console.error(`Failed to retrieve data. Status code: ${response.statusCode}`);
  }
});
