import wx
import CodePbo2

class MyPin(CodePbo2.MyFrame1):
    def __init__(self,parent):
        CodePbo2.MyFrame1.__init__(self,parent)

app = wx.App()
frame = MyPin (parent=None)
frame.Show()
app.MainLoop()