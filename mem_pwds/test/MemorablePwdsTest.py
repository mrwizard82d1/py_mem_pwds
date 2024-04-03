#! env python

import math
import re
import string
import unittest

import MemorablePwds

class MemorablePwdsTest(unittest.TestCase):
    "Executes unit tests of the MemorablePwds class."

    def isStrongEnough(self, thePassword, theAttackSpace=50.4):
        """Determines if the password is strong enough."""
        firstWord, secondWord = re.split('[^A-Za-z]', thePassword)
        if len(firstWord) >= 6 and len(secondWord) >= 6 and len(thePassword) >= 14:
            return True
        else:
            return False
    
    def isValidFormat(self, thePassword):
        """Determine if thePassword has a valid format."""
        validPattern = '^[A-Za-z]+[^A-Za-z-][A-Za-z]+$'
        validMatcher = re.compile(validPattern)
        return validMatcher.match(thePassword)
        
    def setUp(self):
        "Set up the test fixtures."
        self._defaultGenerator = MemorablePwds.MemorablePwds()

    def testFormat(self):
        "Verifies the format of the returned password."
        for i in range(0, 99):
            theNextPwd = next(self._defaultGenerator)
            self.assertTrue(self.isValidFormat(theNextPwd),
                            'Invalid default password format: %s' % theNextPwd)
            self.assertTrue(self.isStrongEnough(theNextPwd),
                            'Insufficiently strong password: %s' % theNextPwd)


if __name__ == '__main__':
    unittest.main();
