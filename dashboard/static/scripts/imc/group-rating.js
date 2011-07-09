jQuery(document).ready(function ($) {
    function bind_delete_button(form) {
        form.find('input[id$=DELETE]').hide();
        form.find('label[for$=DELETE]').click(function () {
            form.slideUp(300);
            // TODO: need to add the person back to the drop downs here
        });
    }

    function add_inline_form(prefix) {
        var count = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val(), 10);
        var last_form = $('.' + prefix + ':last');

        var new_form = last_form.clone(false).html(last_form.html().replace(
                new RegExp(prefix + '-\\d-', 'g'), prefix + '-' + count + '-'));
        bind_delete_button(new_form);

        // remove the selected option of the last form from the available options
        option = last_form.find(':selected').val();
        if (option.length) {
            new_form.find('option[value="' + option + '"]').remove();
        }

        // remove and re-initialise the stars
        new_form.find('.star-rating, .star-rating-control').remove();
        new_form.find('.rating input').removeAttr('class').removeAttr('style').removeAttr('checked').rating();

        new_form.hide().insertAfter(last_form).slideDown(300);

        // Update the total form count
        $('#id_' + prefix + '-TOTAL_FORMS').val(count + 1);
        return false;
    }

    // Remove a selected user from all the other select boxes
    $('.field select').live('change', function () {
        selected = $(this).val();
        $('.field select').not($(this)).each(function () {
            $(this).children('option[value="' + selected + '"]').remove();
        });
    });

    // Bind the delete buttons
    $('.inline-form').each(function () {
        return bind_delete_button($(this));
    });

    // Setup the add form button
    $('.add-inline').click(function () {
        return add_inline_form('rating_set');
    });
});

