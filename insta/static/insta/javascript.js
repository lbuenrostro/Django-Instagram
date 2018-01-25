$('.panel-body').toggle();

$('.panel-heading').on('click', function() {
    var parent = $(this).parent();
    var body = $(parent).find('.panel-body');
    $(body).toggle();
});
