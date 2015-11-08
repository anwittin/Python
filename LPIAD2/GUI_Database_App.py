import wx, GUI_database


class Frame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None, title=title, size=(800, 600))
        panel = wx.Panel(self)

        # create the menu bar
        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()
        exitItem = fileMenu.Append(wx.NewId(), "Exit")
        menuBar.Append(fileMenu, "File")

        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.exitProgram, exitItem)

        self.CreateStatusBar()

        # Setup add new character ui
        # Create static box
        wx.StaticBox(panel, label='Add a new character', pos=(20, 30), size=(280, 190))

        # text for name, gender, etc
        wx.StaticText(panel, label='Name:', pos=(30, 60))
        wx.StaticText(panel, label='Gender:', pos=(30, 90))
        wx.StaticText(panel, label='Age:', pos=(30, 120))
        wx.StaticText(panel, label='Occupation:', pos=(30, 150))

        # Single line text boxes
        self.sName = wx.TextCtrl(panel, size=(150, -1), pos=(130, 60))
        self.sGen = wx.TextCtrl(panel, size=(150, -1), pos=(130, 90))
        self.sAge = wx.SpinCtrl(panel, value='0', size=(70, 25), pos=(130, 120))
        self.sOcc = wx.TextCtrl(panel, size=(150, -1), pos=(130, 150))

        # Save button
        save = wx.Button(panel, label="Create Character", pos=(100, 185))
        save.Bind(wx.EVT_BUTTON, self.updateCharacter)


        # Setup update character

        wx.StaticBox(panel, label='Add Character', pos=(20, 240), size=(280, 190))

        # text for name, gender, etc
        wx.StaticText(panel, label='Name:', pos=(30, 270))
        wx.StaticText(panel, label='Gender:', pos=(30, 300))
        wx.StaticText(panel, label='Age:', pos=(30, 330))
        wx.StaticText(panel, label='Occupation:', pos=(30, 360))

        # Single line text boxes
        self.sName = wx.TextCtrl(panel, size=(150, -1), pos=(130, 270))
        self.sGen = wx.TextCtrl(panel, size=(150, -1), pos=(130, 300))
        self.sAge = wx.SpinCtrl(panel, value='0', size=(70, 25), pos=(130, 330))
        self.sOcc = wx.TextCtrl(panel, size=(150, -1), pos=(130, 360))

        # Save button
        save = wx.Button(panel, label="Update Character", pos=(100, 420))
        save.Bind(wx.EVT_BUTTON, self.updateCharacter)



        # Setup the Table UI
        # Setup table as listCtrl
        self.listCtrl = wx.ListCtrl(panel, size=(400,400), pos=(350,40), style=wx.LC_REPORT | wx.BORDER_SUNKEN)

        # Add Columns to the listCtrl
        self.listCtrl.InsertColumn(0, "ID")
        self.listCtrl.InsertColumn(1, "Name")
        self.listCtrl.InsertColumn(2, "Gender")
        self.listCtrl.InsertColumn(3, "Age")
        self.listCtrl.InsertColumn(4, "Occupation")

        self.fillListCtrl()
        # Run onSelect funciton when item is selected
        self.listCtrl.Bind(wx.EVT_LIST_ITEM_SELECTED, self.onSelect)

        # Delete Button
        deleteBtn = wx.Button(panel, label="Delete", pos=(640, 450))

        # Bind the delete button to onDelete functino
        deleteBtn.Bind(wx.EVT_BUTTON, self.onDelete)


    def addCharacter(self, event):
        name = self.sName.GetValue()
        gen = self.sGen.GetValue()
        age = self.sAge.GetValue()
        occ = self.sOcc.GetValue()


        # Checking if variables have values
        if (name == '') or (gen == '') or (age == '') or (occ == ''):
            # Alert the user a variable is empty
            dlg = wx.MessageDialog(None, 'Some character details are missing. Please enter values in each text'
                                         'box.', 'Missing Details', wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
            return False

    # Adding character to database
        GUI_database.newCharacter(name, gen, age, occ)
        print GUI_database.viewAll()
        # Clear boxes
        self.sName.Clear()
        self.sGen.Clear()
        self.sAge.SetValue(0)
        self.sOcc.Clear()


        self.fillListCtrl()
    def exitProgram(self, event):
	
        self.Destroy()

    def fillListCtrl(self):

        allData = GUI_database.viewAll()
        self.listCtrl.DeleteAllItems()
        for row in allData:
            self.listCtrl.Append(row)

    def onSelect(self, event):
        self.onSelectId = event.GetText()

    def onDelete(self, event):
        # Delete the character
        GUI_database.deleteCharacter(self.onSelectId)
        self.fillListCtrl()
    def updateCharacter(self, event):
        pass



app = wx.App()
frame = Frame("Python GUI")
frame.Show()
app.MainLoop()
