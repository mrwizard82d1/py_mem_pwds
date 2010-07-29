"""Module defining the MemorablePwds class."""


import math
import os
import random
import re
import string
import sys


class DictionaryNotFoundError(Exception): pass


class MemorablePwds:
    "Generates easily memorizable strong passwords."

    def __init__(self, theSeed = None):
        "Construct a generator for memorable and strong passwords."
        source = self.findDictionary()
        self._words = map(string.strip, source.readlines())
        random.seed(theSeed)

    def buildPassword(self):
        """Build the password from its components: a word, a separator
        and a second word."""
        return '%s%s%s' % (self.nextWord(), self.nextSeparator(),
                           self.nextWord()) 

    def calcAttackSpace(self, thePassword):
        """Calculates the average attack space of thePassword. This
        function bases this calculation on the analysis performed by
        Robert E. Smith in _Authentication_."""
        searchSpace = self.calcSearchSpace(thePassword)
        likelihood = 1
        return (math.log(self.calcSearchSpace(thePassword) /
                         (2 * likelihood)) / math.log(2))

    def calcSearchSpace(self, thePassword):
        """Calculates the search space for thePassword. The search
        space is the number of combinations that an attacker needs to
        search using trial-and-error."""
        [firstWord, secondWord] = re.split('[^A-Za-z]', thePassword)
        return (self.calcWordSpace(firstWord) *
                self.calcSeparatorSpace() *
                self.calcWordSpace(secondWord)) 

    def calcSeparatorSpace(self):
        """Calculate the search space due to the separator
        character."""
        return (len(string.digits + string.punctuation) - len('-'))

    def calcWordSpace(self, theWord):
        """Calculate the search space for a single word."""
        return len(self._words)

    def findDictionary(self):
        """Finds the dictionary file using the Python search path."""
        theBasename = os.path.join('dict.txt')
        theFilename = os.path.join('mem_pwds', 'etc', theBasename)
        for dirname in sys.path:
            candidate = os.path.join(dirname, theBasename)
            if os.path.isfile(candidate):
                return open(candidate, 'rt')
            candidate = os.path.join(dirname, theFilename)
            if os.path.isfile(candidate):
                return open(candidate, 'rt')
        raise DictionaryNotFoundError('%s not found on Python search path.' % theBasename)
    
    def isStrongEnough(self, thePassword, theAttackSpace=50.4):
        """Determine if thePassword is 'strong enough.'"""
        firstWord, secondWord = re.split('[^A-Za-z]', thePassword)
        return (len(firstWord) >= 6 and len(secondWord) >= 6 and len(thePassword) > 14)

    def isValidSeparator(self, theChar):
        """Determine if the specified character is a valid separator
        for a strong password. Valid separators are digits and
        punctuation marks (except for the dash)."""
        if theChar in string.digits:
            return theChar
        elif ((theChar in string.punctuation) and
              (theChar != '-')):
            return theChar
        else:
            return 0

    def isValidWord(self, theWord):
        """Determine if theWord is valid. A word is valid if it
        contains only alphabetic characters."""
        thePattern = '^[A-Za-z]+$'
        theMatcher = re.compile(thePattern)
        return theMatcher.match(theWord)

    def next(self):
        "Return the next memorable but strong password."
        thePassword = self.buildPassword()
        while (not self.isStrongEnough(thePassword)):
            thePassword = self.buildPassword()
        return thePassword

    def nextChar(self):
        "Generate a random ascii character."
        return chr(random.randrange(0, 127))

    def nextSeparator(self):
        """Generate the next random, single character separator."""
        theChar = self.nextChar()
        while (not self.isValidSeparator(theChar)):
            theChar = self.nextChar()
        return theChar
            
    def nextWord(self):
        """Generate the next random word."""
        theWord = random.choice(self._words)
        while (not self.isValidWord(theWord)):
            theWord = random.choice(self._words)
        return theWord

