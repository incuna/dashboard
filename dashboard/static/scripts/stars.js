jQuery(document).ready(function($) {
    if ($('#current-rating')) {
        //var rating = $('#movie-rating');
        //$('#movie-rating').remove();
        $('#rating input[type="radio"]').rating();//'select', rating.val());
    } else {
        $('#rating input[type="radio"]').rating();
    }
});
