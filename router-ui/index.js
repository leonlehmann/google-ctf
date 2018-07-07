var express = require('express');
var app = express();

app.get('/', function (req, res) {
  console.log(req.query.session);
  res.send(200);
});

app.use('/static', express.static('static'));

app.listen(3000, function () {
  console.log('Example app listening on port 3000!');
});
