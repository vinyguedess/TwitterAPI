import unittest
from src import TwitterAPI


class TwitterAPITest(unittest.TestCase):

    def testAuthentication(self):
        """ Python 3
        Testing TwitterAPI Authentication
        """
        consumer_key = 'wmanKvXVpvBtanMbIllPqg'
        consumer_secret = 'OLb7k1rCEsfzGesoZHj75rZbRnrxmgiNDwmjzaW9Y'
        self.assertIsInstance(TwitterAPI(consumer_key, consumer_secret), TwitterAPI)

    def testGetRequests(self):

        self.assertTrue(True)
