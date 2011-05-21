jQuery(document).ready(function($) {
    var page = '#page';

    function load_alert() {
        $.get('/twitterstream/alert/', null,
        function(data) {
            $(page + ' #alert').replaceWith(data);
        });
    }

    function load_holidaycal() {
        $.get('/holidaycal/', null,
        function(data) {
            $(page + ' #holidaycal').replaceWith(data);
        });
    }

    function load_imc() {
        $.get('/movie-club/widget/', null,
        function(data) {
            $(page + ' #imc').replaceWith(data);
        });
    }

    function load_redmine_graphs() {
        console.log('loading graphs');
        $.get('/redmine/graphs/', null,
        function(data) {
            $(page + ' #graphs').replaceWith(data);
        });
    }

    function load_redmine_list() {
        $.get('/redmine/list/', null,
        function(data) {
            $(page + ' #list').replaceWith(data);
        });
    }

    function load_shoppinglist() {
        $.get('/shopping-list/', null,
        function(data) {
            $(page + ' #shoppinglist').replaceWith(data);
        });
    }

    function load_tweetstream() {
        $.get('/twitterstream/teamincuna/', null,
        function(data) {
            $('#ticker1 ul').append(data);
            $('#ticker1').ticker();
            $('#ticker2').ticker();
        });
    }

    function load_weather() {
        $.get('/weather/', null,
        function(data) {
            $(page + ' #weather').replaceWith(data);
        });
    }

    function load_scrollable() {
        $(".scrollable").scrollable();
    }

    function load_all() {
        //load_alert();
        //load_holidaycal();
        load_imc();
        //load_redmine_graphs();
        //load_redmine_list();
        load_shoppinglist();
        //load_tweetstream();
        load_weather();
        //load_scrollable();
        $(page + ' #time').text(new Date().toString());
    }

    load_all();

    // Reload every 3 minutes
    window.setInterval(function() {
        load_tweetstream();
        load_shoppinglist();
    }, 180000);

    // Reload every 30 minutes
    window.setInterval(function() {
        load_redmine_graphs();
        load_redmine_list();
    }, 1800000);

    // Reload every hour
    window.setInterval(function() {
        load_imc();
        load_weather();
    }, 3600000);

    // Reload every 3 hours
    window.setInterval(function() {
        load_holidaycal();
    }, 10800000);

    $('#rating .star').rating();
});

