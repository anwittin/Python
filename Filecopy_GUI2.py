import wx, wx.lib.filebrowsebutton
import wx.lib.agw.multidirdialog as MDD
import os
class Frame(wx.Frame):
	def __init__(self, title):
		wx.Frame.__init__(self, None, wx.ID_ANY,
                          "File and Folder Dialogs Tutorial")
		panel = wx.Panel(self, wx.ID_ANY)
		self.currentDirectory = os.getcwd()
		menuBar = wx.MenuBar()
		fileMenu = wx.Menu()
		editMenu = wx.Menu()
		helpMenu = wx.Menu()
		exitItem = fileMenu.Append(wx.NewId(), "Exit")
		menuBar.Append(fileMenu, "File")
		menuBar.Append(editMenu, "Edit")
		menuBar.Append(helpMenu, "Help")
 
        # create the buttons and bindings
		openFileDlgBtn = wx.Button(panel, label="Show OPEN FileDialog")
		openFileDlgBtn.Bind(wx.EVT_BUTTON, self.onOpenFile)
		self.SetMenuBar(menuBar)
		self.Bind(wx.EVT_MENU, self.exitProgram, exitItem)
		
		self.CreateStatusBar()
		
				
		# Buttons
		browseSrc = wx.Button(panel, label="Source", 
									pos = (20, 27))
		browseSrc.Bind(wx.EVT_BUTTON, self.onOpenFile)
		browseDst = wx.Button(panel, label="Destination", 
									pos = (20, 87))
		manualChk = wx.Button(panel, label = "Manually Check", 
									pos = (20, 147))
	
	#----------------------------------------------------------------------
	def onOpenFile(self, event):
		"""
		Create and show the Open FileDialog
		"""
		
		dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultDir=self.currentDirectory, 
            defaultFile="",
            #wildcard=wildcard,
            style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR)
		if dlg.ShowModal() == wx.ID_OK:
			paths = dlg.GetPaths()
			print "You chose the following file(s):"
			for path in paths:
				print path
		dlg.Destroy()
 
    #----------------------------------------------------------------------
	
	
	
	
	
	
	def exitProgram(self, event):
		self.Destroy()
		
		
		
		
app = wx.App()
frame = Frame("File Copy GUI")
frame.Show()
app.MainLoop()


# # Lables and tags
#		wx.StaticBox(panel, label = 'Browse Source', 
#					pos = (10, 10), size = (365, 50))
#		wx.StaticBox(panel, label = 'Browse Destination', 
#					pos = (10, 70), size = (365, 50))
#		wx.StaticBox(panel, label = 'Manually Check File Status', 
#					pos = (10, 130), size = (365, 50))