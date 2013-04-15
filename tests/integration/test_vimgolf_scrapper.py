from services.vimgolf import VimGolfScraper
import unittest2 as unittest

class VimGolfTest(unittest.TestCase):
  def test_should_understand_vimgolf(self):
    vimgolf = VimGolfScraper()
    self.assertIn("www.vimgolf.com", vimgolf.url())