#!/usr/bin/env python


import wx
import mem_pwds.MemorablePwds


class Panel(wx.Panel):
    """The main panel for the application."""

    def __init__(self, parent):
        """Construct the instance."""
        super(Panel, self).__init__(parent)

        self._candidates = []
        self._generator = mem_pwds.MemorablePwds.MemorablePwds()

        # Create the interface.
        panel1 = wx.ScrolledWindow(self)
        candidate_text = wx.TextCtrl(panel1, style=wx.TE_MULTILINE)
        candidate_text.SetBackgroundColour('red')
        self.FitInside()
        panel2 = wx.ScrolledWindow(self)
        sample_text = wx.TextCtrl(panel2, style=wx.TE_MULTILINE)
        self.FitInside()
        sample_text.SetBackgroundColour('green')

        # Layout the interface.
        sizer = wx.GridSizer(rows=1, cols=2)
        sizer.Add(panel1, 0, wx.EXPAND)
        sizer.Add(panel2, 0, wx.EXPAND)
        self.SetSizer(sizer)
        self.Fit()


class Frame(wx.Frame):
    """The main window for the application."""

    def __init__(self, **kwargs):
        """Initialize the frame of this application."""
        super(Frame, self).__init__(**kwargs)

        # Create the view.
        self.menu_bar = self.CreateMenuBar()
        self.SetMenuBar(self.menu_bar)
        
        self.status_bar = self.CreateStatusBar()
        self.panel = Panel(self)

    def CreateMenuBar(self):
        """Create the menu bar."""
        menu_bar = wx.MenuBar()
        
        file_menu = wx.Menu()
        new_menu_item = file_menu.Append(wx.NewId(), '&New')
        self.Bind(wx.EVT_MENU, self.OnClear, new_menu_item)
        file_menu.AppendSeparator()
        exit_menu_item = file_menu.Append(wx.NewId(), 'E&xit')
        self.Bind(wx.EVT_MENU, self.OnExit, exit_menu_item)
        menu_bar.Append(file_menu, '&File')

        edit_menu = wx.Menu()
        generate_menu_item = edit_menu.Append(wx.NewId(), '&Generate')
        self.Bind(wx.EVT_MENU, self.OnGenerate, generate_menu_item)
        clear_menu_item = edit_menu.Append(wx.NewId(), 'C&lear')
        self.Bind(wx.EVT_MENU, self.OnClear, clear_menu_item)
        menu_bar.Append(edit_menu, '&Edit')
        
        return menu_bar

    def OnClear(self, event):
        """Respond to a clear request."""
        print('{0}.OnClear() called'.format(self.__class__))

    def OnCloseWindow(self, event):
        """Respond to closing this window."""
        self.Destroy()

    def OnExit(self, event):
        """Respond to an exit request."""
        self.Close(True)

    def OnGenerate(self, event):
        """Respond to a generate request."""
        self._candidates = [self._generator.next() for i in range(8)]


class App(wx.App):
    """The wxPython application."""

    def __init__(self):
        """Construct an instance."""
        
        # Suppress redirection to see output in console.
        super(App, self).__init__(redirect=False)

    def OnInit(self):
        """To be performed at application initialization."""

        self.frame = Frame(parent=None, title='Memorable Passwords')
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True


def main():
    """Single (externally callable) entry point."""
    app = App()
    app.MainLoop()


if __name__ == '__main__':
    main()
