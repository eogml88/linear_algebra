let express = require('express');
let app = express();
let ejs = require('ejs');
const main_display = require('./main_display.json');
const port = process.env.PORT || 3000;

app.use(express.static('public'))
app.set('view engine', 'ejs');

app.get('/', (req, res) => {
  res.render('index', {main_display: main_display});
});

app.listen(port);