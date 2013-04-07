from urllib import urlencode, urlopen
import json

class RottenTomatoesAPI:
	def __init__(self, api_key='[replace-with-api-key]', version=1.0):
		self.api_key = api_key
		self.base_url = self.base = 'http://api.rottentomatoes.com/api/public/v%s/' % (version)
		self.format = '.json'
		self.end_url = self.format + '?apikey=' + self.api_key

	def set(self, *args):
		self.base_url = self.base + '/'.join(args) + "/" if args else self.base
		return self

	def build_url(self, url_string, **kwargs):
		return (self.base_url + url_string).rstrip("/") + self.end_url + self.querystring(**kwargs)

	def querystring(self, **kwargs):
		return "&" + urlencode(kwargs) if kwargs else ''

	def __call__(self, *args, **kwargs):
		return self.fetch(self.build_url('/'.join(args), **kwargs))

	def get(self, *args, **kwargs):
		return self.__call__(*args, **kwargs)

	def custom(self, url, **kwargs):
		return self.fetch(self.build_url(url, **kwargs))

	def fetch(self, url):
		return json.loads(urlopen(url).read())

