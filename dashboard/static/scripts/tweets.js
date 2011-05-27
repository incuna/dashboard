jQuery(document).ready(function($){

    var ticker;
    var tweet_div = '#ticker';

    function load_tweetstream() {

        function build_tweet(id, avatar, text) {
            return $('<li><img src="'+avatar+'" height="48" width="48"><span id ="'+id+'" class="text">'+text+'</span></li>');
        }

        function load_initial_tweets(tweets) {
            $.each(tweets, function(index, tweet) {
                $(tweet_div + ' ul').append(build_tweet(tweet.id, tweet.user.profile_image_url, tweet.text));
            });
        }

        $.ajax('https://api.twitter.com/1/incuna/lists/teamincuna/statuses.json?callback=?', {
            crossDomain: true,
            dataType: 'jsonp',
            success: function(data) {
                tweets = data.slice(0, 3);
                if (!$(tweet_div + ' li').length) {
                    load_initial_tweets(tweets);
                    ticker = $(tweet_div).ticker(pxpersec=500);
                } else {
                    if (tweets[0].id != $(tweet_div + ' li:first .text')[0].id) {
                        old_tweets = $(tweet_div + ' li');
                        console.log(old_tweets);
                        $.each(tweets, function(index, tweet) {
                            ticker.addMsg(build_tweet(tweet.id, tweet.user.profile_image_url, tweet.text));
                        });
                        old_tweets.each(function() {
                            ticker.removeMsg($(this));
                        });
                    }
                }
            }
        });
    }

    window.setInterval(function() {
        load_tweetstream();
    }, 180000);
    load_tweetstream();
});

