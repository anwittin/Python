import wx

class Frame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None, title=title, size=(500,450))
        panel = wx.Panel(self)
        wx.StaticBox(panel, label='Simpsons Family Selector', pos=(10,10), size=(460,370))
        wx.StaticText(panel, label='Simpsons Characters', pos=(75,30))
        simpsons =['Bart', 'Lisa', 'Maggie', 'Marge', 'Homer']
        cb = wx.ComboBox(panel, pos=(100, 50), choices = simpsons, style=wx.CB_READONLY)
        wx.CheckBox(panel, label='Male', pos=(20, 100))
        wx.CheckBox(panel, label='Female', pos=(20, 120))
        wx.RadioButton(panel, label='Male', pos=(200, 100))
        wx.RadioButton(panel, label='Female', pos=(200, 120))
        button = wx.Button(panel, label="Exit", size=(50, 20), pos=(410, 350))
        button.Bind(wx.EVT_BUTTON, self.exit)
        wx.TextCtrl(panel, size=(300, -1), pos=(20,150))
        wx.TextCtrl(panel, style=wx.TE_MULTILINE, size=(300, 200), pos=(20, 175))
        wx.SpinCtrl(panel, value='0', pos=(320, 105), size=(70, 25))
        sc = wx.SpinCtrl(panel, value='0', pos=(320, 50), size=(70, 25))
        sc.Bind(wx.EVT_SPINCTRL, self.spinControl)
        self.valueText = wx.StaticText(panel, label='00', pos=(130,80))
        # Create menu bar
        menuBar = wx.MenuBar()

        # Create the menus
        fileMenu = wx.Menu()
        editMenu = wx.Menu()

        # Add Items to the file menu
        fileMenu.Append(wx.NewId(), "New File", "Create a new file")
        fileMenu.Append(wx.NewId(), "Open")
        exitItem = fileMenu.Append(wx.NewId(), "Exit")
        self.Bind(wx.EVT_MENU, self.exit, exitItem)

        # Add Items to the edit menu
        editMenu.Append(wx.NewId(), "Copy")
        editMenu.Append(wx.NewId(), "Cut")
        editMenu.Append(wx.NewId(), "Paste")

        # Add file and edit to the menu
        menuBar.Append(fileMenu, "File")
        menuBar.Append(editMenu, "Edit")

        self.SetMenuBar(menuBar)

    def exit(self, event):
        self.Destroy()

    def spinControl(self, event):
        #Get spin control value
        value = event.GetPosition()
        #Update static text
        self.valueText.SetLabel(str(value))

app = wx.App()
frame = Frame("wxPython Widgets!")
frame.Show()
app.MainLoop()
