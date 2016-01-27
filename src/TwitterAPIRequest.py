import urllib.request, urllib.parse, gzip
from .TwitterAPIResponse import TwitterAPIResponse


class TwitterAPIRequest:

    _allowedRequestMethods = ['GET', 'POST', 'PUT', 'DELETE']  # Define allowed request methods

    _url = None
    _data = {}
    _method = 'GET'
    _header = {}

    def __init__(self, url, data={}, method='GET', header={}):
        """Python

        :param url:
        :param data:
        :param method:
        :return:
        """

        self.set_url(url)
        self.set_data(data)
        self.set_method(method)
        self.set_header(header)

    def set_url(self, url):

        self._url = url

    def set_data(self, data):

        if isinstance(data, dict) is True:
            self._data = data

    def set_method(self, method):

        if method in self._allowedRequestMethods:
            self._method = method

    def set_header(self, header):

        self._header = header

    def prepare_request(self):
        """Python 3
        Prepare Request object

        :return: Request
        """

        # Treat header codification
        has_encoding = False
        for key, value in self._header.items():
            if key.lower() == 'accept-encoding' and value == 'gzip':
                has_encoding = True

        if not has_encoding:
            self._header['Accept-Encoding'] = 'gzip'

        # Treat DATA that will be sent to server
        data_to_be_sent = urllib.parse.urlencode(self._data).encode('ascii')

        # Treat URL that will be requested
        url_requested = "https://api.twitter.com%s" % self._url

        if data_to_be_sent != b'':
            return urllib.request.Request(url_requested, data_to_be_sent, self._header)
        else:
            return urllib.request.Request(url_requested, headers=self._header)

    def request(self):
        """ Python 3
        Makes request to the server

        :return: TwitterAPIResponse
        """

        try:
            response_from_request = urllib.request.urlopen(self.prepare_request())

            return TwitterAPIResponse(response_from_request)
        except Exception as ex:
            print(ex)
            return False
