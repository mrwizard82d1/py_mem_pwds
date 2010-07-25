#! env python
#

"""An interactive, text-based application to generate strong, easily memorized passwords."""

import cmd
import os
import string
import sys

projectsDir = os.path.join('D:', os.sep, 'Documents', 'Professional', 'Projects')
dictDir = os.path.join(projectsDir, 'MemorablePwds')
pathRoots = [ projectsDir, dictDir ]
def configPythonPath(roots=pathRoots):
    """Configures the python search path."""
    for root in roots:
        sys.path.append(root)
configPythonPath()

import MemorablePwds.MemorablePwds

class MemorablePwdsApp(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = 'Memorable Passwords: '
        self._generator = MemorablePwds.MemorablePwds.MemorablePwds()

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
    try:
        theApp.cmdloop()
    except "EOF":
        pass


if __name__ == '__main__':
    doApp()

