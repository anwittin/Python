import wx, shutil, os, datetime as DT, time

class Frame(wx.Frame):
	def __init__(self, title):
		wx.Frame.__init__(self, None, wx.ID_ANY, title=title, size=(400, 300))
		panel = wx.Panel(self, wx.ID_ANY)
		self.currentDirectory = os.getcwd()
		
		# Menu bar and functionality
		menuBar = wx.MenuBar()
		fileMenu = wx.Menu()
		editMenu = wx.Menu()
		helpMenu = wx.Menu()
		exitItem = fileMenu.Append(wx.NewId(), "Exit")
		menuBar.Append(fileMenu, "File")
		menuBar.Append(editMenu, "Edit")
		menuBar.Append(helpMenu, "Help")
		
		self.SetMenuBar(menuBar)
		self.Bind(wx.EVT_MENU, self.exitProgram, exitItem)
		
		self.CreateStatusBar()
		
				
		# Buttons
		browseSrc = wx.Button(panel, label="Source", pos = (20, 27))
		browseSrc.Bind(wx.EVT_BUTTON, self.onOpenFile)
		
		browseDst = wx.Button(panel, label="Destination", pos = (20, 87))
		browseDst.Bind(wx.EVT_BUTTON, self.onOpenFile)
		
		manualChk = wx.Button(panel, label = "Manually Check", pos = (20, 147))
		manualChk.Bind(wx.EVT_BUTTON, self.manualCheck)
		
		
	def onOpenFile(self, event):
		"""
		Create and show the Open FileDialog
		"""
		dlg = wx.FileDialog(
			self, message="Choose a file",
			defaultDir=self.currentDirectory, 
			defaultFile="",
			style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR)
		if dlg.ShowModal() == wx.ID_OK:
			paths = dlg.GetPaths()
			print "You chose the following file(s):"
			for path in paths:
				print path
		
		dlg.Destroy()

	def exitProgram(self, event):
		self.Destroy()
		
	def manualCheck(self, event):
		source = "C:\\Folder A\\"
		dest = "C:\\Folder B\\"
		files = os.listdir(source)
		files.sort()
		t1 = time.time()
		for f in files:
			f[0]
			src = source +f
			f1 = os.path.getmtime(src)
			if t1 - f1 < 86400: 
				dst = dest +f
				shutil.move(src, dst)
				print "File '%s' has changed in the last 24 hours\n moving from %s to %s " %(f, source, dest)
				time.sleep(.75)
			else:
				print "File '%s' has not been modified in last 24 hours" %f
				time.sleep(.5)
		
		
		
app = wx.App()
frame = Frame("File Copy GUI")
frame.Show()
app.MainLoop()