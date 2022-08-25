const express = require('express')
const app = express()
const port = 3000
const path = require('path')

app.use(express.static(__dirname + '/site'));

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/site/index.html')
})

app.use(express.static(__dirname + '/site/files/weather4you/build/'));

app.get('/weather4you', (req, res) => {
  res.sendFile(__dirname + '/site/files/weather4you/build/index.html')
})

app.get('/test', (req, res) => {
  res.send("hello world")
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})