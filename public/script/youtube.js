function videos(videoId) {
    var first = '<h1><strong>' + videoId + '</strong></h1>'
    var iframe = '<iframe style="margin-bottom: 10px; border: 1px solid red; border-radius: 5px" width="100%" height="100%" src="https://www.youtube.com/embed/' + videoId + '"></iframe>'
    this.grid = $('.grid-stack').data('gridstack')
    var node = {
        x: 3,
        y: 3,
        width: 5,
        height: 4,
    }
    var elementId = 'id="' + videoId + '"'
    var valueID = 'value="' + videoId + '"'
    var button = '<form action="/deleteWidget" method="POST"><input type="hidden" name="toRemove" ' + valueID + '></input><button type="submit" class="trashButton"></button></form>'
    var createElement = '<div class="grid-stack-item" ' + elementId + ' style="background-color: grey; margin: 10px; border-radius: 10px;"><i style="position:absolute; top:3px; right: 4px"></i><button id="editButton" class="editButton" onclick="editWidget(this.parentNode.id)"></button><div class="grid-stack-item-content" style="padding: 20px; text-align: center">' + button + first + iframe + '</div></div>'
    this.grid.addWidget($(createElement), node.x, node.y, node.width, node.height, node.name)
}

function views(videoId) {
    var apiKey = 'AIzaSyDbB8TFiUCVdenG1rk8ObLdBQFkTIMwtBw'
    var url = "https://www.googleapis.com/youtube/v3/videos?part=statistics&id=" + videoId + "&key=" + apiKey
    fetch(url)
    .then(function(resp) {
        return resp.json()
    })
    .then(function(data) {
        var elementId = 'id="' + videoId + '"'
        var reloadId = 'h2' + videoId + ''
        var statistics = data.items[0].statistics
        var first = '<h1><strong>' + videoId + '</strong></h1>'
        var second = '<h2 id="' + reloadId + '"><label>Nb of views :</label> ' + statistics.viewCount + '</h2>'
        this.grid = $('.grid-stack').data('gridstack')
        var node = {
            x: 3,
            y: 3,
            width: 4,
            height: 2,
        }
        var valueID = 'value="' + videoId + '"'
        var button = '<form action="/deleteWidget" method="POST"><input type="hidden" name="toRemove" ' + valueID + '></input><button type="submit" class="trashButton"></button></form>'
        var createElement = '<div class="grid-stack-item" ' + elementId + ' style="background-color: grey; margin: 10px; border-radius: 10px;"><i style="position:absolute; top:3px; right: 4px"></i><button id="editButton" class="editButton" onclick="editWidget(this.parentNode.id)"></button><div class="grid-stack-item-content" style="padding: 20px; text-align: center">' + button + first + second + '</div></div>'
        this.grid.addWidget($(createElement), node.x, node.y, node.width, node.height, node.name)
    })
}

function LikesandDislikes(videoId) {
    var apiKey = 'AIzaSyDbB8TFiUCVdenG1rk8ObLdBQFkTIMwtBw'
    var url = "https://www.googleapis.com/youtube/v3/videos?part=statistics&id=" + videoId + "&key=" + apiKey
    fetch(url)
    .then(function(resp) {
        return resp.json()
    })
    .then(function(data) {
        var statistics = data.items[0].statistics
        var likes = statistics.likeCount
        var dislikes = statistics.dislikeCount
        var reloadIdOne = 'h2Likes' + videoId
        var reloadIdTwo = 'h2dislikes' + videoId
        var first = '<h1><strong>' + videoId + '</strong></h1>'
        var second = '<h2 id="' + reloadIdOne + '"><label>Nb of likes :</label> ' + likes + '</h2>'
        var secondBis = '<h2 id="' + reloadIdTwo + '"><label>Nb of dislikes :</label> ' + dislikes + '</h2>'
        this.grid = $('.grid-stack').data('gridstack')
        var node = {
            x: 3,
            y: 3,
            width: 4,
            height: 2,
        }
        var elementId = 'id="' + videoId + '"'
        var valueID = 'value="' + videoId + '"'
        var button = '<form action="/deleteWidget" method="POST"><input type="hidden" name="toRemove" ' + valueID + '></input><button type="submit" class="trashButton"></button></form>'
        var createElement = '<div class="grid-stack-item" ' + elementId + ' style="background-color: grey; margin: 10px; border-radius: 10px;"><i style="position:absolute; top:3px; right: 4px"></i><button id="editButton" class="editButton" onclick="editWidget(this.parentNode.id)"></button><div class="grid-stack-item-content" style="padding: 20px; text-align: center">' + button + first + second + secondBis + '</div></div>'
        this.grid.addWidget($(createElement), node.x, node.y, node.width, node.height, node.name)
    })
}