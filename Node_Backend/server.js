var express = require('express');
var url= require('url');
// var mongodb = require('mongodb').MongoClient;
var bodyParser = require('body-parser');
var app = express();
var cors = require('cors');
app.use(cors());
// var dbo;
// var url = "mongodb://localhost/";
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.get('/health', (req, res) => {
    res.send('Response from Node Backend Server - Abinav');
});
app.use(function (req, res, next) {        
    res.setHeader('Access-Control-Allow-Origin', 'http://localhost:4200');    
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE');    
    res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type');      
    res.setHeader('Access-Control-Allow-Credentials', true);       
    next();  });
app.listen(8080);
