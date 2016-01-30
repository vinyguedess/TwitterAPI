import gzip
import json


class TwitterAPIResponse:

    _response = ''
    _GZipEncoded = True
    _header = None

    def __init__(self, response, gzip_encoded=True):
        """ Python 3
        TwitterAPIResponse constructor

        :param response: str
        :param gzip_encoded: bool
        """

        self._response = response
        self._GZipEncoded = gzip_encoded

    def mount_header(self):
        """ Python 3
        Mount Response HEADER converting into a dictionary
        """

        headers = {}
        for item in str(self._response.info()).split('\n'):
            h = item.split(':')
            if len(h) > 1 or h[0] != '':
                headers[h[0]] = h[1]

        self._header = headers

    def get_headers(self, header=None):
        """ Python 3
        Get response headers

        :param header: str
        :return: dict
        """

        if not isinstance(self._header, dict):
            self.mount_header()

        if header is not None:
            for key, value in self._header.items():
                if key.lower() == header.lower():
                    return value

        return self._header

    def get_body(self, raw=False):

        body = self._response.read()

        # In case response is encoded as GZIP, make decompress
        if self._GZipEncoded is True:
            body = gzip.decompress(body)

        content_type = self.get_headers('content-type')

        # In case response isn't raw and response's content type is JSON
        if raw is False and content_type.find('/json') >= 0:
            return json.loads(body.decode('utf8', 'ignore'))

        return body.decode('utf8', 'ignore')
