jQuery(document).ready(function ($) {
    var star = $('input[type="radio"]');
    star.rating();
    if ($('#current-rating').length) {
        var rating = $('#movie-rating');
        $('#movie-rating').remove();
        star.rating('select', rating.text());
        star.rating('disable');
    }
});

