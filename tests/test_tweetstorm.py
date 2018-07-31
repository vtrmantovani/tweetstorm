import pytest

from tweetstorm import Tweetstorm
from tweetstorm.exceptions import TweetstormException


@pytest.fixture
def small_text():
    return "A common trope in discussions about startups & " \
           "venture capital is a potential misalingnment of " \
           "incentives between startup team."


@pytest.fixture
def small_text_tweetstorm():
    return [
        "1/1 A common trope in discussions about startups & "
        "venture capital is a potential misalingnment of "
        "incentives between startup team."
    ]


@pytest.fixture
def medium_text():
    return "A common trope in discussions about startups & " \
           "venture capital is a potential misalingnment of " \
           "incentives between startup team & investors. " \
           "I don't think this percevied missalignment actually " \
           "exists in most.maybe all casses -- and I Want to explain why."


@pytest.fixture
def medium_text_tweetstorm():
    return [
        "1/2 A common trope in discussions about startups & "
        "venture capital is a potential misalingnment of "
        "incentives between startup team &",
        "2/2 investors. I don't think this percevied missalignment actually "
        "exists in most.maybe all casses -- and I Want to explain why."
    ]


@pytest.fixture
def big_text():
    return "A common trope in discussions about startups & " \
           "venture capital is a potential misalingnment of " \
           "incentives between startup team & investors. " \
           "I don't think this percevied missalignment actually " \
           "exists in most.maybe all casses -- and I Want to explain why. " \
           "The argumment goes, ""When you take VC, you have to shoot " \
           "for the moon; smaller outcomes that may be great for " \
           "the team are precluded."


@pytest.fixture
def big_text_tweetstorm():
    return [
        '1/3 A common trope in discussions about startups & '
        'venture capital is a potential misalingnment of '
        'incentives between startup team &',
        "2/3 investors. I don't think this percevied missalignment actually "
        "exists in most.maybe all casses -- and I Want to explain why. The",
        '3/3 argumment goes, When you take VC, you have to shoot for the '
        'moon; smaller outcomes that may be great for the team are precluded.'
    ]


class TestTweetstorm:

    def test_generate_small_text(self, small_text, small_text_tweetstorm):
        t = Tweetstorm(small_text)
        assert t.generate() == small_text_tweetstorm

    def test_generate_medium_text(self, medium_text, medium_text_tweetstorm):
        t = Tweetstorm(medium_text)
        assert t.generate() == medium_text_tweetstorm

    def test_generate_big_text(self, big_text, big_text_tweetstorm):
        t = Tweetstorm(big_text)
        assert t.generate() == big_text_tweetstorm

    def test_generate_without_text(self):
        with pytest.raises(TweetstormException) as e:
            t = Tweetstorm()
            t.generate()

        assert str(e.value) == "Please set a text"

    def test_create_tweets_without_text(self):
        with pytest.raises(TweetstormException) as e:
            t = Tweetstorm()
            t._create_tweets("")

        assert str(e.value) == "Please set a text to" \
                               " generate the tweets"

    def test_show_tweets_without_text(self):
        with pytest.raises(TweetstormException) as e:
            t = Tweetstorm()
            t._show_tweets([])

        assert str(e.value) == "Please set a list of tweets"
