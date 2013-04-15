from services.vimgolf import VimGolfScraper


class Snooper(object):
  def main(self):
    scraper = VimGolfScraper()
    scraper.challenges()


if __name__ == '__main__':
  Snooper().main()
