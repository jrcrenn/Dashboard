const express = require('express');
const router = express.Router();

router.get('/', function (req, res) {
    res.redirect('/login');
});

router.get('/login', function (req, res) {
    res.sendFile('/app/views/login.html');
});

router.get('/dashboard', function (req, res) {
    res.sendFile('/app/views/dashboard.html');
});

router.get('/about.json', function (req, res) {
    res.sendFile('/app/about.json');
});

module.exports = router;