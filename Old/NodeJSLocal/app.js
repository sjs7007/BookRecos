var express = require('express');
var app = express();
var exec = require("child_process").exec;

app.use(express.bodyParser());

app.get('/hello.txt', function(req, res){
	res.send('Hello World');
});

app.get('/Output.xml', function(req, res){
	res.set('Content-Type','text/xml');
	res.sendfile('Output.xml');
});


app.set('views', __dirname + '/views');
app.engine('html', require('ejs').renderFile);
app.get('/', function (req, res)
{
    res.render('StartPage.html');
});

app.post('/isbnResult', function (req, res)
{
    var command = "python Final.py "+req.body.isbnNumber;
    exec(command, function (error, stdout, stderr) {
    	res.render('Final2.html');
	});
});


var server = app.listen(process.env.PORT||3000, function() {
	console.log('Listening on port %d', server.address().port);
});