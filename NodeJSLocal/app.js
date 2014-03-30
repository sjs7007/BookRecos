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
app.get('/', function (req, res)
{
    res.render('StartPage.html');
});

app.get('/v2', function (req, res)
{
    res.render('Final2.html');
});

app.get('/v3', function (req, res)
{
    res.render('Final3.html');
});




app.post('/myaction', function(req, res) {
  console.log(req.body.emailJK);
  res.send(req.body.emailJK)
});



var server = app.listen(3000, function() {
	console.log('Listening on port %d', server.address().port);
});