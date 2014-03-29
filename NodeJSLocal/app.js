var express = require('express');
var app = express();
var exec = require("child_process").exec;


app.get('/hello.txt', function(req, res){
	res.send('Hello World');
});

app.get('/ISBNSearch', function(req, res){
	console.log("Request handler 'ISBNSearch' was called.");
	var content = "empty";
	exec("python Final.py 9780007369683", function (error, stdout, stderr) {
	content = stdout;
	res.send(content);


	});
});


app.set('views', __dirname + '/views');
app.engine('html', require('ejs').renderFile);
app.get('/v1', function (req, res)
{
    res.render('Final.html');
});

app.get('/v2', function (req, res)
{
    res.render('Final2.html');
});

app.get('/v3', function (req, res)
{
    res.render('Final3.html');
});



var server = app.listen(3000, function() {
	console.log('Listening on port %d', server.address().port);
});