from services.vimgolf import VimGolfScraper
from snooper import Snooper
import unittest2 as unittest

class SnooperTest(unittest.TestCase):
  def test_should_understand_vimgolf_page(self):
    vim_golf = VimGolfScraper();
    # snooper = Snooper(vim_golf)
