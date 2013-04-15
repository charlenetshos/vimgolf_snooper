import sys
from services.vimgolf import VimGolfScraper


class Snooper(object):

  def __init__(self, out=sys.stdout):
    self.out = out

  def _length_of_longest(self, challenges):
    lengths_of_challenges_titles = sorted([len(challenge['title']) for challenge in challenges], reverse=True)
    return max(lengths_of_challenges_titles)

  def _print(self,output):
    self.out.write(output.format('Challenge', 'Entries') + "\n")

  def formatter(self, challenges):
    MIN_SPACE = 5
    output = "{0:<%s} {1}" % (gself._length_of_longest(challenges) + MIN_SPACE)

    self._print(output)
    self._print(output.format(''.ljust(len('Challenge'), '-'), ''.ljust(len('Entries'), '-')))

    for challenge in challenges:
      self._print(output.format(challenge['title'], challenge['entries']))

  def main(self):
    challenges = VimGolfScraper().challenges()
    self.formatter(challenges)


if __name__ == '__main__':
  Snooper().main()
