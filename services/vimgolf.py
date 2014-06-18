import re
import urllib
from bs4 import BeautifulSoup

class VimGolfScraper(object):
  def __init__(self):
    self.URL = 'http://www.vimgolf.com'
    self.ENCODING = 'utf-8'

  def url(self):
    return self.URL

  def _get(self, tag, attrs):
    soup = BeautifulSoup(urllib.urlopen(self.URL))
    return soup.find_all(tag, attrs=attrs)

  def extract_number_of_entries(self, entries):
    number_of_entries = re.findall('\d+', entries)
    return number_of_entries[0]

  def _format(self, data):
    return data.encode(self.ENCODING)

  def _get_challenge_content(self, header):
    content = header.find_all(text=True)
    anchor_title = self._format(content[1])
    number_of_entries = self._format(self.extract_number_of_entries(content[2]))
    return anchor_title, int(number_of_entries)

  def challenges(self):
    headers = self._get('h5', {'class': 'challenge'})
    all_challenges = []
    for header in headers:
      anchor_title, number_of_entries = self._get_challenge_content(header)
      all_challenges.append({'title': anchor_title, 'entries': number_of_entries})

    all_challenges.sort(key=lambda challenge: challenge['entries'], reverse=True)
    return all_challenges

