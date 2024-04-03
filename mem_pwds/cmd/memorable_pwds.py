#!/usr/bin/env python
#

"""An interactive, text-based application to generate strong, easily
memorized passwords.""" 

import cmd
import os
import string
import sys


try:
    # if it is installed
    from mem_pwds.MemorablePwds import MemorablePwds
except ImportError:
    # if it is in development
    sys.path.append(os.path.join(os.path.split(os.path.abspath(__file__))[0],
                                               '..', '..'))
    from mem_pwds.MemorablePwds import MemorablePwds


class MemorablePwdsApp(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = 'Memorable Passwords: '
        self._generator = MemorablePwds()

    def help_next(self):
        print('Generates the next password.')
    def do_next(self, theCount):
        print(next(self._generator))
        
    def help_EOF(self):
        print('Quits the program.')
    def do_EOF(self, line):
        return True
        
    def help_exit(self):
        print('Quits the program.')
    def do_exit(self, line):
        if __name__ == '__main__':
            sys.exit()
        else:
            raise Exception('exit')
        

def doApp():
    theApp = MemorablePwdsApp()
    theApp.cmdloop()


if __name__ == '__main__':
    doApp()

