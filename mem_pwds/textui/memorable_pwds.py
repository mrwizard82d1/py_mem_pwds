#! /usr/bin/env python
#

"""An interactive, text-based application to generate strong, easily
memorized passwords.""" 

import cmd
import os
import string
import sys


# Add parent directory to path.
sys.path.append('..')

from mem_pwds.MemorablePwds import MemorablePwds


class MemorablePwdsApp(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = 'Memorable Passwords: '
        self._generator = MemorablePwds()

    def help_next(self):
        print 'Generates the next password.'
    def do_next(self, theCount):
        print self._generator.next()
        
    def help_EOF(self):
        print 'Quits the program.'
    def do_EOF(self, line):
        if __name__ == '__main__':
            sys.exit()
        else:
            raise "EOF"
        
    def help_exit(self):
        print 'Quits the program.'
    def do_exit(self, line):
        if __name__ == '__main__':
            sys.exit()
        else:
            raise "exit"
        

def doApp():
    theApp = MemorablePwdsApp()
    theApp.cmdloop()


if __name__ == '__main__':
    doApp()

