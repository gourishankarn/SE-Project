$(function () {
    $('#test').click(function () {
        $('.test').modal('show');
    });

    $('#test2').click(function () {
        $('.test').modal('show');
    });
    $('.ui.menu a.item').on('click', function () {
        $(this)
            .addClass('active')
            .siblings()
            .removeClass('active');
    })
});
