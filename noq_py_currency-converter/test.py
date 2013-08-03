#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

In this example, we create a simple
window in PyQt4.

author: Jan Bodnar
website: zetcode.com 
last edited: October 2011
"""

#!/usr/bin/python

# simple.py

import wx

app = wx.App()

frame = wx.Frame(None, -1, 'main.py')
frame.Show()

app.MainLoop()