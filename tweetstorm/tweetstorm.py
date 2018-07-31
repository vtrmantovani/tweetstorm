from .exceptions import TweetstormException


class Tweetstorm(object):

    def __init__(self, text=None, limit=140):
        self.text = text
        self.limit = limit

    def generate(self):
        if not self.text:
            raise TweetstormException("Please set a text")

        list_tweet = self._create_tweets(self.text)
        tweets = self._show_tweets(list_tweet)
        return tweets

    def _create_tweets(self, text):
        if not text:
            raise TweetstormException(
                "Please set a text to generate the tweets"
            )

        words = text.split()
        tweet = ''
        list_tweets = []

        # Set limit of characters less the format of text "index/total text"
        limit = self.limit - 5

        total_words = len(words)
        for i, elem in enumerate(words):
            this_word = elem
            next_word = words[(i + 1) % total_words]
            tweet += this_word
            if len(tweet + next_word) > limit:
                list_tweets.append(tweet)
                tweet = ''
            else:
                if i == len(words) - 1:
                    list_tweets.append(tweet)
                else:
                    tweet += ' '

        return list_tweets

    def _show_tweets(self, list_tweets):
        if not list_tweets:
            raise TweetstormException("Please set a list of tweets")

        total = len(list_tweets)
        tweets = []

        for i, tweet in enumerate(list_tweets, start=1):
            tweets.append("{}/{} {}".format(i, total, tweet))

        return tweets
