jQuery(document).ready(function($) {
    $('.field select').change(function() {
        selected = $(this).val();
        $('.field select').not($(this)).each(function() {
            $(this).children('option[value="'+selected+'"]').remove();
        });
    });
    $('input:radio').rating();
});
