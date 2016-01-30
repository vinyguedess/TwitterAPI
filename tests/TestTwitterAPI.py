import unittest
from src import TwitterAPI, TwitterAPIResponse


class TestTwitterAPI(unittest.TestCase):
    """ Python 3

    Class responsible for implementing tests on whole API
    """

    _API = None

    def setUp(self):
        """ Python 3
        Set up test before it runs
        """

        consumer_key = 'CONSUMER_KEY'
        consumer_secret = 'CONSUMER_SECRET'
        self._API = TwitterAPI(consumer_key, consumer_secret, app_name='MyTwitterAPI')

    def test_authentication(self):
        """ Python 3
        Testing TwitterAPI Authentication
        """

        # Test if is authenticated before authenticate to receive FALSE
        self.assertFalse(self._API.is_authenticated())

        # Test if authentication works
        self.assertTrue(self._API.authenticate_application())

        # Test if authenticated expecting a TRUE response now because authentication was made above
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
