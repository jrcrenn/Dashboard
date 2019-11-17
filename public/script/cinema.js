function movies(movieName) {
    var apiKey = "ffc922e2714e6b51e8f4b18511cb50b2"
    var url = "https://api.themoviedb.org/3/search/movie?api_key=" + apiKey + "&query=" + movieName
    fetch(url)
    .then(resp => resp.json())
    .then (data => {
        var movieInformation = data.results[0]
        var title = movieInformation.original_title
        var note = movieInformation.vote_average
        var img = '<img style="border: 1px solid transparent; border-radius: 5px" src="http://image.tmdb.org/t/p/w300/' + movieInformation.poster_path + '">'
        var first = '<h2>' + title + '</h2>'
        var second = '<h3 style="margin-top: 10px"><strong><label>Stars :</label> ' + note + '</strong></h3>'
        var secondBis = '<h3><strong><label>Release date :</label> ' + movieInformation.release_date + '</strong></i></h3>'
        var secondBisBis = '<h3><strong><label>Entry number :</label> ' + movieInformation.popularity + '</strong></i></h3>'
        this.grid = $('.grid-stack').data('gridstack')
        var node = {
            x: 3,
            y: 3,
            width: 4,
            height: 7,
        }
        var elementId = 'id="' + movieName + '"'
        var valueID = 'value="' + movieName + '"'
        var button = '<form action="/deleteWidget" method="POST"><input type="hidden" name="toRemove" ' + valueID + '></input><button type="submit" class="trashButton"></button></form>'
        var createElement = '<div class="grid-stack-item" ' + elementId + ' style="background-color: grey; margin: 10px; border-radius: 10px;"><i style="position:absolute; top:3px; right: 4px"></i><button id="editButton" class="editButton" onclick="editWidget(this.parentNode.id)"></button><div class="grid-stack-item-content" style="padding: 20px; text-align: center">' + button + img + second + secondBis + secondBisBis + '</div></div>'
        this.grid.addWidget($(createElement), node.x, node.y, node.width, node.height)
    })
}