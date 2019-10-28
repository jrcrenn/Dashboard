var User = require('./model/user.js');

module.exports = function (app, passport, request, nodeWidget, fs) {

    app.get('/', function (req, res) {
        res.redirect('/login');
    });

    app.get('/login', function (req, res) {
        res.sendFile('/app/views/login.html', {
            message: req.flash('loginMessage')
        });
    });

    app.post('/login', passport.authenticate('local-login', {
        successRedirect: '/dashboard',
        failureRedirect: '/login',
        failureFlash: true
    }));

    app.get('/register', function (req, res) {
        res.sendFile('/app/views/login.html');
    });

    app.post('/register', passport.authenticate('local-signup', {
        successRedirect: '/',
        failureRedirect: '/register',
        failureFlash: true
    }));

    app.get('/dashboard', isLoggedIn, function (req, res, next) {
        res.sendFile('/app/views/dashboard.html');
    });

    app.get('/:username/:password', function (req, res) {
        var newUser = new User();
        newUser.local.username = req.params.username;
        newUser.local.password = req.params.password;
        console.log(newUser.local.username + " " + newUser.local.password);
        newUser.save(function (err) {
            if (err)
                throw err;
        });
        res.send("Success!");
    });

    app.get('/logout', function (req, res) {
        req.logout();
        res.redirect('/');
    });

    app.get('/about.json', function (req, res) {
        res.sendFile('/app/about.json');
    });
};

function isLoggedIn(req, res, next) {
    if (req.isAuthenticated()) {
        return next();
    }
    res.redirect('/login');
}