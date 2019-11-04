var express = require('express');
var app = express();
var port = 8080;

var MongoClient = require('mongodb').MongoClient;

var url = 'mongodb://localhost/stackoverflow';

var str = "";

app.route('/jobs').get(function(req, res){

    MongoClient.connect(url, function(err, database){
        var stackDB = database.db('stackoverflow');
        var cursor = stackDB.collection('questions').find({});
        str = "";
        cursor.forEach(function(item){
            if(item != null){
                str = str + "<table>" + "<tr>" + "<td>" + " || " + " Company: " + item.company + "</td>" + "<td>" + " || " + " Title: " + item.title + "</td>" + "<td>" + " || " + " Posted: " + item.posted +  " || " + "</td>" + "</br>" + "</tr>" + "</table>";
            }
        }, function(err){
            res.send(str);
            database.close();
        }
        );
    });
});

var server = app.listen(port, function(){
    console.log('listening on *:' + port);
});
