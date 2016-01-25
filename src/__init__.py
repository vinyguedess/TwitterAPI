

class TwitterAPI:

	def __init__(self, consumer_key=None, consumer_secret=None):
		"""Python 3
		TwitterAPI Constructor

		:param consumer_key: str
		:param consumer_secret: str
		"""

		self._consumerKey = consumer_key
		self._consumerSecret = consumer_secret