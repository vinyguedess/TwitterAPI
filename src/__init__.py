

class TwitterAPI():

	consumerKey = None
	consumerSecret = None

	def __init__(self, consumerKey=None, consumerSecret=None):

		self._consumerKey = consumerKey
		self._consumerSecret = consumerSecret

