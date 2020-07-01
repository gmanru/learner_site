const axios = require("axios");


axios.get("http://127.0.0.1:8000/people/api/student/")
  .then(response => console.log("response", response.data))

fetch('http://127.0.0.1:8000/course/api/')
  .then(response => response.json())
  .then(data => console.log(data));