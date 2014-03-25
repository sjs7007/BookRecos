var express = require('express')//express dependency 

var app = express.createServer(); //initialize server/create app

app.set('view engine', 'ejs'); //specify template engine
app.set('views', __dirname + '/views'); //location of template files
app.set('view options', { layout: false });

/*Routes*/
app.get('/', function (req, res) {
res.render('index');
});

//Listen
app.listen(4000);


