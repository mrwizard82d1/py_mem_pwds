#!/usr/bin/env python


import wx
import mem_pwds.MemorablePwds


window_size = (768, 480)


class View(wx.ScrolledWindow):
    """The main panel for the application."""

    def __init__(self, parent):
        """Construct the instance."""
        super(View, self).__init__(parent)

        self._candidates = []
        self._generator = mem_pwds.MemorablePwds.MemorablePwds()

        self.SetScrollbars(1, 1, window_size[0], window_size[1])

        self.createWindows()
        self.layoutWindows()

        self.SetSizer(self.view_sizer)
        self.Fit()

    def add_candidates(self):
        """Add candidate passwords."""
        self._candidates.extend([self._generator.next() for
                                 i in range(8)])
        self.candidate_view.Clear()
        self.candidate_view.AppendText('\n'.join(self._candidates))

    def clear(self):
        """Clear candidate passwords."""
        self._candidates = []
        self.candidate_view.Clear()
        self.candidate_view.AppendText('\n'.join(self._candidates))

    def createWindows(self):
        """Create the child windows of this Panel."""
        self.candidate_label = wx.StaticText(self, wx.ID_ANY,
                                             'Candidate passwords:')
        self.candidate_view = wx.TextCtrl(self, size=(window_size[0] / 2,
                                                      window_size[1]),
                                          style=wx.TE_MULTILINE)
        self.candidate_view.SetBackgroundColour('red')

        self.try_it_label = wx.StaticText(self, wx.ID_ANY, "Try 'em!")
        self.try_it_view = wx.TextCtrl(self, size=(window_size[0] / 2,
                                                   window_size[1]),
                                       style=wx.TE_MULTILINE)
        self.try_it_view.SetBackgroundColour('green')

    def layoutWindows(self):
        """Layout the child indows of this Panel."""
        candidate_sizer = wx.BoxSizer(wx.VERTICAL)
        candidate_sizer.Add(self.candidate_label, 0, flag=wx.EXPAND)
        candidate_sizer.Add(self.candidate_view, 1, flag=wx.EXPAND)

        try_it_sizer = wx.BoxSizer(wx.VERTICAL)
        try_it_sizer.Add(self.try_it_label, 0, flag=wx.EXPAND)
        try_it_sizer.Add(self.try_it_view, 1, flag=wx.EXPAND)

        self.view_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.view_sizer.Add(candidate_sizer, 1, flag=wx.EXPAND)
        self.view_sizer.Add(try_it_sizer, 1, flag=wx.EXPAND)


class Frame(wx.Frame):
    """The main window for the application."""

    def __init__(self, **kwargs):
        """Initialize the frame of this application."""
        super(Frame, self).__init__(**kwargs)

        # Create the view.
        self.menu_bar = self.CreateMenuBar()
        self.SetMenuBar(self.menu_bar)
        
        self.status_bar = self.CreateStatusBar()
        self.view = View(self)

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
        self.view.clear()

    def OnCloseWindow(self, event):
        """Respond to closing this window."""
        self.Destroy()

    def OnExit(self, event):
        """Respond to an exit request."""
        self.Close(True)

    def OnGenerate(self, event):
        """Respond to a generate request."""
        self.view.add_candidates()


class App(wx.App):
    """The wxPython application."""

    def __init__(self):
        """Construct an instance."""
        
        # Suppress redirection to see output in console.
        super(App, self).__init__(redirect=False)

    def OnInit(self):
        """To be performed at application initialization."""

        self.frame = Frame(parent=None, title='Memorable Passwords',
                           size=window_size)
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True


def main():
    """Single (externally callable) entry point."""
    app = App()
    app.MainLoop()


if __name__ == '__main__':
    main()
