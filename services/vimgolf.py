import re
import urllib
from bs4 import BeautifulSoup

class VimGolfScraper(object):
  def __init__(self):
    self.URL = 'http://www.vimgolf.com'
    self.ENCODING = 'utf-8'
    self.soup = BeautifulSoup(urllib.urlopen(self.URL))


  def url(self):
    return self.URL

  def _get(self, tag, attrs):
    return self.soup.find_all(tag, attrs=attrs)

  def extract_number_of_entries(self, entries):
    number_of_entries = re.findall('\d+', entries)
    return number_of_entries[0]

  def _get_challenge_content(self, header):
    content = header.find_all(text=True)
    anchor_title = content[1]
    number_of_entries = self.extract_number_of_entries(content[2])
    return anchor_title, number_of_entries

  def challenges(self):
    headers = self._get('h5', {'class': 'challenge'})
    for header in headers:
      anchor_title, number_of_entries = self._get_challenge_content(header)

      print (anchor_title.encode(self.ENCODING), ": ", number_of_entries.encode(self.ENCODING))
