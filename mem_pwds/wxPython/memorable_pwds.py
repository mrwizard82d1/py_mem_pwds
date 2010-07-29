#! python


import wx


if __name__ == '__main__':
    app = wx.App(False)
    frame = wx.Frame(None, wx.ID_ANY, 'Memorable Passwords')
    frame.Show(True)
    app.MainLoop()
