#! env python

"""Generate strong, memorable passwords using the Tcl/Tk interface."""

import os
import sys
projectsDir = os.path.join('D:', os.sep, 'Documents',
                           'Professional', 'Projects')
dictDir = os.path.join(projectsDir, 'MemorablePwds')
pathRoots = [ projectsDir, dictDir ]
def configPythonPath(roots=pathRoots):
    """Configures the python search path."""
    for root in roots:
        sys.path.append(root)
configPythonPath()

import pp2e_laj.gui.tools.guimixin
import pp2e_laj.gui.tools.guimaker
import mem_pwds.MemorablePwds

from Tkinter import *
from ScrolledText import ScrolledText

class MemorablePwdsApp(pp2e_laj.gui.tools.guimixin.GuiMixin,
                       pp2e_laj.gui.tools.guimaker.GuiMakerWindowMenu):
    """(Tkinter) User interface for memorable passwords application."""

    def clear(self):
        """Clear all the candidate passwords."""
        self._candidates = []
        self.refreshCandidates()
    
    def generate(self):
        """Generates a set of candidate passwords."""
        for i in range(0, 8):
            self._candidates.append(self._generator.next())
        self.refreshCandidates()

    def help(self):
        pp2e_laj.gui.tools.guimaker.GuiMakerWindowMenu.help(self)

    def makeWidgets(self):
        middle = Frame(self)
        middle.pack(expand=YES, fill=BOTH)

        Label(middle, text='Candidate Passwords').grid(row=0,
                                                       column=0,
                                                       sticky=NSEW)
        self.candidatesView = ScrolledText(middle, height=15, width=45)
        self.candidatesView.config(font=('courier', 10, 'normal'))
        self.candidatesView.grid(row=1, column=0, sticky=NSEW)

        Label(middle, text='Try It!').grid(row=0, column=1, sticky=NSEW)
        self.scratchPadView = ScrolledText(middle, height=15, width=45)
        self.scratchPadView.config(font=('courier', 10, 'normal'))
        self.scratchPadView.grid(row=1, column=1, sticky=NSEW)

    def refreshCandidates(self):
        self.candidatesView.delete('1.0', END)
        for word in self._candidates:
            self.candidatesView.insert(END, word + '\n')
            
    def start(self):
        """Initialize the menu bar and tool bar of the application."""

        self._candidates = []
        self._generator = mem_pwds.MemorablePwds.MemorablePwds()
        self.menuBar = [
            ('File', 0, [('New', 0, self.clear),
                         ('Exit', 0, sys.exit)]),
            ('Edit', 0, [('Generate', 0, self.generate)]),
            ]
        self.toolBar = [
            ('Generate', self.generate, {'side': LEFT}),
            ('Clear', self.clear, {'side': LEFT}),
            ]


def main():
    """Invoke the Tcl/Tk main loop."""
    MemorablePwdsApp().mainloop()


if __name__ == '__main__':
    main()
