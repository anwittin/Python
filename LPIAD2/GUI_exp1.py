import wx


class Frame(wx.Frame):
    # Add title parameter
    def __init__(self, title):
        wx.Frame.__init__(self, None, title=title, size=(300, 200))
        self.Center()
        self.Move((400, 400))
        panel = wx.Panel(self)
        button = wx.Button(panel, label="Exit", size=(100, 40), pos=(90, 90))
        button.Bind(wx.EVT_BUTTON, self.exit)

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
        self.CreateStatusBar()

    def exit(self, event):
        self.Destroy()


app = wx.App()
frame = Frame("Python GUI")
frame.Show()
app.MainLoop()
