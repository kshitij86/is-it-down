import requests
from urllib.parse import urlparse


def check_url(site):
	try:
		result = urlparse(site)
		return all([result.scheme, result.netloc, result.path])
	except:
		return False

def check_site(site):
	try:
		response = requests.get(str(site))
		return [response.status_code, response.status_code == 200]
	except:
		return [404, False]