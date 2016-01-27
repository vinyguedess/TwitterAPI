import unittest
from src import TwitterAPI, TwitterAPIResponse


class TestTwitterAPI(unittest.TestCase):

    _API = None

    def setUp(self):

        consumer_key = 'wmanKvXVpvBtanMbIllPqg'
        consumer_secret = 'OLb7k1rCEsfzGesoZHj75rZbRnrxmgiNDwmjzaW9Y'
        self._API = TwitterAPI(consumer_key, consumer_secret, app_name='TwitterAPI')

    def test_authentication(self):
        """ Python 3
        Testing TwitterAPI Authentication
        """

        # Test if authentication works
        self.assertTrue(self._API.authenticate_application())

    def test_user_requests(self):
        """Python 3

        Testing TwitterAPI User's methods
        """

        # Getting user information
        user_info = self._API.get_user_info('Viny_Guedes')
        self.assertIsInstance(user_info, TwitterAPIResponse)
        self.assertIsInstance(user_info.get_body(), dict)

        # Getting user timeline
        user_timeline = self._API.get_user_timeline('Viny_Guedes')
        self.assertIsInstance(user_timeline, TwitterAPIResponse)
        self.assertIsInstance(user_timeline.get_body(), list)

        # Getting user followers
        user_followers = self._API.get_user_followers('Viny_Guedes')
        self.assertIsInstance(user_followers, TwitterAPIResponse)
        self.assertIsInstance(user_followers.get_body(), dict)

    def test_tweet_requests(self):
        """Python 3

        Testing TwitterAPI Tweet's methods
        """

        # Test search method
        search_posts = self._API.search_tweet('SONOOO', count=3, result_type='recent')
        self.assertIsInstance(search_posts, TwitterAPIResponse)
        self.assertIsInstance(search_posts.get_body(), dict)
