const express = require('express')
const app = express()
const port = 3000
const path = require('path')

app.use(express.static(__dirname + '/site'));

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/site')
})

app.get('/pgh-buildings', (req, res) => {
  res.sendFile(__dirname + '/site/projects/pgh-buildings.html')
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})