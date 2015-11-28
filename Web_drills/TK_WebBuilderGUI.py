
from tkinter import *
import codecs, os

class Window(Frame):
	def __init__(self, master = None):
		Frame.__init__(self, master)
		self.master = master
		
		self.init_window()
	def init_window(self):
		global txt
		self.master.title("Website Updater")
		self.pack(fill = BOTH, expand = 1)
		#Button Section
		createButton = Button(self, text="Create Page", command=self.getText)
		createButton.place(x=10, y=180)
		showPage = Button(self, text="Show Page", command=self.showPage)
		showPage.place(x=90, y=180)
		menu = Menu(self.master)
		self.master.config(menu=menu)
		
		# File button on the menu
		file = Menu(menu)
		file.add_command(label='Exit', command=self.client_exit)
		menu.add_cascade(label='File', menu=file)
		
		#Edit button on the menu
		#edit = Menu(menu)
	
		#menu.add_cascade(label='Edit', menu=edit)
		
		txt = Text(root, height=6, width=47)
		txt.place(x = 10, y = 50)
		# Label for the input window
		textBox = Label(root, text="Enter Text Below To Update The Webpage.")
		textBox.place(relx=0.5, y = 35, anchor=CENTER)
	def getText(self):
		text = txt.get('1.0', 'end -1c' )
		html1 = '''<!DOCTYPE HTML>
			<html>
			<body>
			<p>%s</p>
			</body>
			</html>
				''' % text
		f = open('summersale.html','w')
		f.write(html1)
		f.close()
		txt.delete("1.0", END)
	def showPage(self):
		page = codecs.open('summersale.html', 'r')
		try:
			os.startfile('summersale.html')
		except AttributeError:
			subprocess.call(['open', 'summersale.html'])
		
	def client_exit(self):
		exit()
		

root = Tk()

root.geometry("400x250")
app = Window(root)
root.mainloop()