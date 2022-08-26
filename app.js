const express = require('express')
const app = express()
const port = 3000
const path = require('path')
const functions = require('firebase-functions');


app.use(express.static(__dirname + '/site'));

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/site/index.html')
})

app.use(express.static(__dirname + '/site/files/weather4you/build/'));


app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})