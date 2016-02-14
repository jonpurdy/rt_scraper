import urllib
import urllib2
from bs4 import BeautifulSoup

def main():

	name = "Casino"

	rating = get_rating(name)
	print("Rating: %s" % rating)

def get_rating(name):

	movie_url = get_url(name)
	rating = get_tomatometer_for_url(movie_url)

	return rating


def get_url(movie_name):
	'''
	Gets the URL for a particular movie
	'''

	import requests
	response = requests.get("http://www.rottentomatoes.com/search/?search=%s" % movie_name, allow_redirects=False)

	soup = BeautifulSoup(response.text, "html.parser")

	table = soup.find("ul",{"id": "movie_results_ul"})

	if table:
		links = table.findAll('a')
		append_url = links[0].get('href')

		
		movie_url = "http://www.rottentomatoes.com%s" % append_url

	else:
		movie_name = movie_name.replace(" ", "_")
		movie_url = "http://www.rottentomatoes.com/m/%s" % movie_name

	return movie_url

def get_tomatometer_for_url(movie_url):
	'''
	Gets the tomatometer rating for the specified URL.
	'''

	user_agent = 'Mozilla/5.0 (Windows NT 6.1; rv:13.0) Gecko/20100101 Firefox/13.0'
	headers = { 'User-Agent' : user_agent }

	try:

		request=urllib2.Request(movie_url, None ,headers)

		response = urllib2.urlopen(request)

		the_page = response.read()

		# parses the page into a beautifulsoup object
		soup = BeautifulSoup(the_page, "html.parser")

		# uses the soup.find function, then 
		# key is itemprop, value is ratingValue
		rating = soup.find("span",{"itemprop":"ratingValue"}).contents

		# returns a list of one item
		return int(rating[0])

	except Exception as e:
		print e
		return 0


if __name__ == '__main__':
	main()
