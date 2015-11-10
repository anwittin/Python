import wx, shutil, sys, os, sqlite3
import datetime as DT, time

# Connect to filecopy database
conn = sqlite3.connect('filecopy.db')

def createTable():
	conn.execute("CREATE TABLE if not exists \
			FILECOPY_INFO( \
			ID INTEGER PRIMARY KEY AUTOINCREMENT, \
			MOD_DATE INTEGER \
			);")
createTable()

def selectManData():
		# Create search string
		manData = "SELECT MOD_DATE from FILECOPY_INFO WHERE ID =(SELECT MAX(ID) FROM FILECOPY_INFO)"
		cursor = conn.execute(manData)
		# get data from table
		mData = [float(record[0]) for record in cursor.fetchall()]
		print mData.strftime('%H:%M:%S')
		return mData
		
selectManData()

class RedirectText:
	def __init__(self, aWxTextCtrl):
		self.out = aWxTextCtrl
	def write(self, string):
		self.out.WriteText(string)
		
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
	
		# Buttons
		browseSrc = wx.Button(panel, label="Source", pos = (10, 10))
		browseSrc.Bind(wx.EVT_BUTTON, self.onOpenFile)
		
		browseDst = wx.Button(panel, label="Destination", pos = (10, 50))
		browseDst.Bind(wx.EVT_BUTTON, self.onOpenFile)
		
		manualChk = wx.Button(panel, label = "Manually Check", pos = (10, 90))
		manualChk.Bind(wx.EVT_BUTTON, self.manualCheck)
		
		# Manual file check status 
		wx.StaticText(panel, label='Last Manual File Check:', pos=(120, 95))
		manChk = wx.TextCtrl(panel, wx.ID_ANY, size=(120, -1), pos=(245, 90))
		
		# Status window for manual file check
		log = wx.TextCtrl(panel, wx.ID_ANY, style=wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL, size=(370, 100), pos=(10, 130))
		
		#add sizer
		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(log, 1, wx.ALL|wx.EXPAND, 5)
		panel.SetSizer(sizer)
		
		#redirect the text
		redir = RedirectText(log)
		sys.stdout=redir
		#manout = mData.strftime('%H:%M:%S')RedirectText(manChk)
		
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
			dst = dest +f
			f1 = os.path.getmtime(src)
			if t1 - f1 < 86400: 
				shutil.move(src, dst)
				print "File '%s' has changed in the last 24 hours.\nMoving from %s to %s " %(f, source, dest)
				time.sleep(.75)		
			else:
				print "File '%s' has not been modified in last 24 hours" %f
				time.sleep(.5)
			
		# Create values part of sql command
		val_str = "'{}'".format(\
			t1)
		sql_str = "INSERT INTO FILECOPY_INFO \
			(MOD_DATE) VALUES ({});".format(val_str)
		conn.execute(sql_str)
		conn.commit()
		return conn.total_changes
		
					

	
app = wx.App()
frame = Frame("File Copy GUI")
frame.Show()
app.MainLoop()