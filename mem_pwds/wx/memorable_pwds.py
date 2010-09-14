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
        text_window_size = (300, 300)
        candidate_label = wx.StaticText(self, wx.ID_ANY,
                                        'Candidate passwords:')
        scroll1 = wx.ScrolledWindow(self, wx.ID_ANY)
        scroll1.SetScrollbars(1, 1, text_window_size[0], text_window_size[1])
        self.candidate_text = wx.TextCtrl(scroll1, size=text_window_size,
                                          style=wx.TE_MULTILINE)
        self.candidate_text.SetBackgroundColour('red')

        try_it_label = wx.StaticText(self, wx.ID_ANY,
                                     'Try it!')
        scroll2 = wx.ScrolledWindow(self)
        scroll2.SetScrollbars(1, 1, text_window_size[0], text_window_size[1])
        sample_text = wx.TextCtrl(scroll2, size=text_window_size,
                                  style=wx.TE_MULTILINE)
        sample_text.SetBackgroundColour('green')

        # Layout the interface.
        candidate_sizer = wx.BoxSizer(wx.VERTICAL)
        candidate_sizer.Add(candidate_label, 0, flag=wx.EXPAND)
        candidate_sizer.Add(scroll1, 1, flag=wx.EXPAND)
        
        try_it_sizer = wx.BoxSizer(wx.VERTICAL)
        try_it_sizer.Add(try_it_label, 0, flag=wx.EXPAND)
        try_it_sizer.Add(scroll2, 1, flag=wx.EXPAND)

        panel_sizer = wx.GridSizer(rows=1, cols=2)
        panel_sizer.Add(candidate_sizer, 0, flag=wx.EXPAND)
        panel_sizer.Add(try_it_sizer, 0, flag=wx.EXPAND)
        self.SetSizer(panel_sizer)
        self.Fit()

    def add_candidates(self):
        """Add candidate passwords."""
        self._candidates.extend([self._generator.next() for
                                 i in range(8)])
        self.candidate_text.Clear()
        self.candidate_text.AppendText('\n'.join(self._candidates))

    def clear(self):
        """Clear candidate passwords."""
        self._candidates = []
        self.candidate_text.Clear()
        self.candidate_text.AppendText('\n'.join(self._candidates))

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
        self.panel.clear()

    def OnCloseWindow(self, event):
        """Respond to closing this window."""
        self.Destroy()

    def OnExit(self, event):
        """Respond to an exit request."""
        self.Close(True)

    def OnGenerate(self, event):
        """Respond to a generate request."""
        self.panel.add_candidates()


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
