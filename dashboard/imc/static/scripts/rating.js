jQuery(document).ready(function($) {
    var star = $('input');
    star.rating();
    if ($('#current-rating')) {
        var rating = $('#movie-rating');
        $('#movie-rating').remove();
        star.rating('select', rating.text());
        star.rating('disable');
    }
});
