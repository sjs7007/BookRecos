var express = require('express');
var app = express();
var exec = require("child_process").exec;

app.use(express.bodyParser());
app.use(express.static(__dirname + '/views')); //so that images inside views folder are included
app.use(express.static(__dirname+'/')); //so that images inside views folder are included

app.get('/hello.txt', function(req, res){
	res.send('Hello World');
});

app.get('/Output.xml', function(req, res){
	res.set('Content-Type','text/xml');
	res.sendfile('Output.xml');
});


app.set('views', __dirname + '/views');
app.engine('html', require('ejs').renderFile);

app.post('/isbnResult', function (req, res)
{
    var command = "python Final.py "+req.body.isbnNumber;
    exec(command, function (error, stdout, stderr) {
    	res.render('Final2.html');
	});
});

app.post('/ratingsInput', function (req, res)
{
    var command = "python recoSite.py "+req.body.input;
    exec(command, function (error, stdout, stderr) {
    	//res.send(stdout);
    	res.render('test42.html');
	});
});

app.get('/', function (req, res)
{
    res.render('test4.html');
});

app.get('/v1', function (req, res)
{
    res.render('StartPage.html');
});

app.get('/v2', function(req, res){
	res.render('test2.html');
});

app.get('/v3', function(req, res){
	res.render('test3.html');
});

app.get('/v4', function(req, res){
	res.render('test4.html');
});


app.get('/v4', function(req, res){
	res.render('test4.html');
});

app.get('/v5', function(req, res){
	res.render('test5.html');
});

var server = app.listen(process.env.PORT||3000, function() {
	console.log('Listening on port %d', server.address().port);
});