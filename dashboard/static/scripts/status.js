jQuery(document).ready(function($) {
    var widgets = {
        'holidaycal': ['/status/holiday-cal/', '#holiday-cal'],
        'movieclub': ['/movie-club/widget/', '#movie-club'],
        'redminegraphs': ['/status/redmine/graphs/', '#graphs'],
        'redminelist': ['/status/redmine/list/', '#list'],
        'shoppinglist': ['/shopping-list/', '#shopping-list'],
        'weather': ['/status/weather/', '#weather']
    };

    function load_widget(url, div) {
        $.get(url, null,
        function(data) {
            $('#page ' + div).replaceWith(data);
            if (div == '#movie-club') {
                $(div + ' .star').rating();
            }
        });
    }

    /* https://api.twitter.com/1/incuna/lists/teamincuna/statuses.atom
     * Might be possible to use the atom feed instead?
     * Would be good to speed this up, it's a bit slow currently.
     * Is append enough? Should we be replacing instead?
     */
    var ticker;
    function load_tweetstream() {
        $.get('/status/twitterstream/teamincuna/', null,
        function(data) {
            $('#ticker ul').append(data);
            ticker = $('#ticker').ticker(pxpersec=500);
        });
    }

    //function load_scrollable() {
        //$(".scrollable").scrollable();
    //}

    for (widget in widgets) {
        load_widget(widgets[widget][0], widgets[widget][1]);
    }
    load_tweetstream();
    //$(page + ' #time').text(new Date().toString());

    //window.setInterval(function() {
        //first = $('.first');
        //ticker.removeMsg($('.first'));
    //}, 1000);

    // Reload every 3 minutes
    window.setInterval(function() {
        load_tweetstream();
        load_widget(widgets.shoppinglist[0], widgets.shoppinglist[1]);
    }, 180000);

    // Reload every 30 minutes
    window.setInterval(function() {
        load_widget(widgets.redminegraphs[0], widgets.redminegraphs[1]);
        load_widget(widgets.redminelist[0], widgets.redminelist[1]);
        load_widget(widgets.weather[0], widgets.weather[1]);
    }, 1800000);

    // Reload every hour
    window.setInterval(function() {
        load_widget(widgets.movieclub[0], widgets.movieclub[1]);
    }, 3600000);

    // Reload every 3 hours
    window.setInterval(function() {
        load_widget(widgets.holidaycal[0], widgets.holidaycal[1]);
    }, 10800000);

    // Need to reload the DOM here.
    $('#rating .star').rating();
});

