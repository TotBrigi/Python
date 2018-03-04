from urllib2 import urlopen
from scraping.BeautifulSoup import BeautifulSoup


url = "http://quotes.yourdictionary.com/theme/marriage/"
response = urlopen(url).read()
soup = BeautifulSoup(response)

quotes = soup.findAll('p', attrs={'class': 'quoteContent'})

for text in quotes:
    print text.string

