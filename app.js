//Setup
const express = require('express');
const bodyParser = require('body-parser');
const MongoClient = require('mongodb').MongoClient;
const PORT = 8080;
const url = "mongodb://mongo:27017/";
const path = require('./routes/routes');
const app = express();

app.use(express.static('public'));
app.use(bodyParser.urlencoded({
    extended: true
}));
app.use('/', path);

//Db connect
MongoClient.connect(url, function (err, db) {
    if (err)
        console.error(err);
    else {
        const dbo = db.db("user");
        dbo.collection("user", function (err, collection) {
            collection.find().toArray(function (err, items) {
                if (err) throw err;
                console.log(items);
            });
        });

        app.post('/register', function (req, res) {
            var email = req.body.email;
            var password = req.body.password;
            var user = {
                email: email,
                pass: password
            };
            dbo.collection("user").insertOne(user, function (err, res) {
                if (err) console.error(err);
                console.log("User added");
            });
            res.redirect('/login');
        });
        app.post('/loginuser', function (req, res) {
            var email = req.body.email;
            var password = req.body.password;
            var user = {
                email: email,
                pass: password
            };
            dbo.collection("user").find(user).count(function (err, count) {
                if (err) throw err;
                if (count >= 1)
                    res.redirect('/dashboard')
                else
                    res.redirect('/login')
            });
        });
    }
});

//Launch listening server on port 8080
app.listen(PORT, function () {
    console.log('App is running')
})
