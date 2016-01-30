from base64 import b64encode
from .TwitterAPIRequest import TwitterAPIRequest
from .TwitterAPIResponse import TwitterAPIResponse


class TwitterAPI:

    _appName = None
    _consumerKey = None
    _consumerSecret = None
    _accessToken = None

    _allowedResultTypes = ['mixed', 'recent', 'popular']

    def __init__(self, consumer_key, consumer_secret, app_name = 'TwitterAPI'):
        """Python 3
        TwitterAPI Constructor
        """

        # Get app information from setup
        self._appName = app_name
        self._consumerKey = consumer_key
        self._consumerSecret = consumer_secret

    def is_authenticated(self):
        """ Python 3
        Checks if application is authenticated

        :return: bool
        """

        return self._accessToken is not None

    def authenticate_application(self):
        """ Python 3
        Authenticates application with Twitter oAuth requirements

        :return: bool
        """

        try:
            # Validates if CONSUMER_KEY was defined
            if self._consumerKey is None:
                raise Exception("You must define a CONSUMER_KEY to continue")

            # Validates if CONSUMER_SECRET was defined
            if self._consumerSecret is None:
                raise Exception("You must define a CONSUMER_SECRET to continue")

            # Generates BEARER_TOKEN
            bearer_token = b64encode(("%s:%s" % (self._consumerKey, self._consumerSecret)).encode('ascii')).decode()

            # Makes request for authentication
            r = TwitterAPIRequest('/oauth2/token', {
                'grant_type': 'client_credentials'
            }, header={
                'Host': 'api.twitter.com',
                'Authorization': 'Basic %s' % bearer_token,
                'Content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                'Content-Length': 29
            }).request()

            # Validates if request worked
            if not isinstance(r, TwitterAPIResponse):
                raise Exception('Error during authentication')

            response = r.get_body()
            self._accessToken = response['access_token']

            return True
        except Exception as ex:
            print(ex.args)
            return False

    def get_user_info(self, user_name):
        """ Python 3
        Gets complete information about defined user

        :param user_name: str
        :return: TwitterAPIResponse
        """

        # Checks if application is already authenticated
        if not self.is_authenticated():
            self.authenticate_application()

        url = '/1.1/users/show.json?screen_name=%s' % user_name

        return TwitterAPIRequest(url, header={
            'Host': 'api.twitter.com',
            'User-Agent': self._appName,
            'Authorization': 'Bearer %s' % self._accessToken
        }).request()

    def get_user_timeline(self, user_name, count=100, include_rts=False):
        """ Python 3
        Returns a dictionary with all tweets from defined user that match requirements

        :param user_name: str
        :param count: int
        :param include_rts: bool
        :return: TwitterAPIResponse
        """

        # Check if already have an ACCESS_TOKEN
        if self.is_authenticated() is False:
            self.authenticate_application()

        url = '/1.1/statuses/user_timeline.json?screen_name=%s' % user_name
        url += '&count=%d&include_rts=%s' % (count, str(include_rts).lower())

        return TwitterAPIRequest(url, header={
            'Host': 'api.twitter.com',
            'User-Agent': self._appName,
            'Authorization': 'Bearer %s' % self._accessToken
        }).request()

    def get_user_followers(self, user_name, count=100, skip_status=False):
        """Python 3
        Get a list of followers from defined user that match the filter requirements

        :param user_name: str
        :param count: int
        :param skip_status: bool
        :return: TwitterAPIResponse
        """

        if self.is_authenticated() is False:
            self.authenticate_application()

        url = '/1.1/followers/list.json?cursor=-1&screen_name=%s' % user_name
        url += '&count=%d&skip_status=%s' % (count, skip_status)

        return TwitterAPIRequest(url, header={
            'Host': 'api.twitter.com',
            'User-Agent': self._appName,
            'Authorization': 'Bearer %s' % self._accessToken
        }).request()

    def search_tweet(self, query, count=100, until=None, geocode=None, lang=None, locale=None, result_type='mixed'):
        """ Python 3

        Returns a list of tweets searched by the matching requirements

        :param query: str
        :param count: int
        :param until: str
        :param geocode: str
        :param lang: str
        :param locale: str
        :param result_type: str
        :return: TwitterAPIResponse
        """

        # Checks if application is already authenticated and authenticates if none
        if self.is_authenticated() is False:
            self.authenticate_application()

        if result_type not in self._allowedResultTypes:
            result_type = 'mixed'

        url = '/1.1/search/tweets.json?q=%s&count=%d&result_type=%s' % (query, count, result_type)
        url += '&until=%s' % until if until is not None else ''
        url += '&geocode=%s' % geocode if geocode is not None else ''
        url += '&lang=%s' % lang if lang is not None else ''
        url += '&locale=%s' % locale if locale is not None else ''

        return TwitterAPIRequest(url, header={
            'Host': 'api.twitter.com',
            'User-Agent': self._appName,
            'Authorization': 'Bearer %s' % self._accessToken
        }).request()
