import sys
from services.vimgolf import VimGolfScraper


class Snooper(object):

  def __init__(self, out=sys.stdout):
    self.out = out

  def _length_of_longest(self, challenges):
    lengths_of_challenges_titles = sorted([len(challenge['title']) for challenge in challenges], reverse=True)
    return max(lengths_of_challenges_titles)

  def _print(self,output):
      try:
        self.out.write(output.format('Challenge', 'Entries') + "\n")
      except:
        # will be leaving app now
        pass


  def _apply_format(self, challenges, min_space):
    output = "{0:<%s} {1}" % (self._length_of_longest(challenges) + min_space)

    self._print(output)
    self._print(output.format(''.ljust(len('Challenge'), '-'), ''.ljust(len('Entries'), '-')))

    for challenge in challenges:
      self._print(output.format(challenge['title'], challenge['entries']))

  def main(self):
    challenges = VimGolfScraper().challenges()
    self._apply_format(challenges, min_space=5)


if __name__ == '__main__':
  Snooper().main()
