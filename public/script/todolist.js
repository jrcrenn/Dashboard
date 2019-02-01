$(document).ready(function () {
    $('#ToDoList #container').animate({ opacity: 1 }, 600, "linear");

    $('#container ul').on('click', 'li', function () {
        $(this).toggleClass('done').blur();
    });

    $('#container ul').on('click', 'span', function (event) {
        $(this).parent().fadeOut(500, function () {
            $(this).remove();
        });
    });

    $('#ToDoList #container .ToDoItems').on('keypress', function (event) {
        if (event.which === 13 && $(this).val() !== "") {
            var newToDo = $(this).val().replace(/</g, "&lt;").replace(/>/g, "&gt;");
            $('#ToDoList #container ul').append('<li><span><i class="fa fa-trash-o"></i></span> ' + newToDo + '</li>')
            $(this).val("").blur();
        }
    });
});