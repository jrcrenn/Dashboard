var express = require('express');
var router = express.Router();
var passport = require('passport')

require('../config/passport')(passport)

var User = require('./model/user')

router.get('/', function (req, res) {
    res.render('login');
});

router.get('/register', function (req, res) {
    res.render('register');
});

router.post('/', (req, res, next) => {
    passport.authenticate('login', {
        successRedirect: '/dashboard',
        failureRedirect: '/',
        failureFlash: true
    })(req, res, next)
})

router.post('/register', (req, res, next) => {
    passport.authenticate('register', {
        successRedirect: '/',
        failureRedirect: '/register',
        failureFlash: true
    })(req, res, next)
})

router.get('/logout', (req, res) => {
    req.logout();
    res.redirect('/');
});

router.get('/auth/facebook', passport.authenticate('facebook', {
    scope: ['public_profile', 'email']
}))

router.get('/auth/facebook/callback', passport.authenticate('facebook', {
    successRedirect: '/dashboard',
    failureRedirect: '/'
}))

router.get('/auth/google', passport.authenticate('google', {
    scope: ['profile', 'email']
}))

router.get('/auth/google/callback', passport.authenticate('google', {
    successRedirect: '/dashboard',
    failureRedirect: '/'
}))

router.get('/dashboard', isLoggedIn, (req, res) => {
    if (req.user.local) {
        widget = req.user.local.widgets
        user = req.user.local
    } else if (req.user.facebook) {
        widget = req.user.facebook.widgets
        user = req.user.facebook
    } else if (req.user.google) {
        widget = req.user.google.widgets
        user = req.user.google
    }
    res.render('dashboard', {
        user: user,
        widgets: widget
    })
})

router.post('/saveWidget', (req, res) => {
    var dataWidget = req.body
    var user = req.user
    var realUser
    if (user.local) {
        realUser = user.local
    } else if (user.facebook) {
        realUser = user.facebook
    }
    realUser.widgets.push(dataWidget)
    user.save()
    res.redirect('/dashboard')
})

router.post('/editWidget', (req, res) => {
    var widgetToChange = req.body.toChange
    var widgetNewValue = req.body.newValue
    var user = req.user
    var realUser
    if (user.local) {
        realUser = user.local
    } else if (user.facebook) {
        realUser = user.facebook
    }
    var widgets = realUser.widgets
    for (var i = 0; i < widgets.length; i++) {
        if (widgets[i].widgetContent == widgetToChange) {
            var newData = {
                widgetContent: widgetNewValue,
                widgetName: widgets[i].widgetName,
                widgetRole: widgets[i].widgetRole
            }
            widgets.splice(i, 1)
            realUser.widgets.push(newData)
            user.save()
            break;
        }
    }
    res.redirect('/dashboard')
})

router.get('/loadWidget', (req, res) => {
    var user = req.user
    var realUser
    if (req.user.local)
        realUser = req.user.local
    else if (req.user.facebook)
        realUser = req.user.facebook
    var widgets = realUser.widgets
    res.send(JSON.stringify(widgets))
})

router.post('/deleteWidget', (req, res) => {
    var widgetToRemove = req.body.toRemove
    var user = req.user
    var realUser
    if (req.user.local)
        realUser = req.user.local
    else if (req.user.facebook)
        realUser = req.user.facebook
    var widgets = realUser.widgets
    for (var i = 0; i < widgets.length; i++) {
        if (widgets[i].widgetContent == widgetToRemove) {
            widgets.splice(i, 1)
            user.save()
            break;
        }
    }
    res.redirect('/dashboard')
})

router.get('/about.json', function (req, res) {
    res.sendFile('about.json', {
        root: '.'
    });
});

function isLoggedIn(req, res, next) {
    if (req.isAuthenticated()) {
        return next();
    }
    res.redirect('/');
}

module.exports = router;