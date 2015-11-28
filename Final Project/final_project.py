from tkinter import *
class Window(Frame):
	def __init__(self, master = None):
		Frame.__init__(self, master)
		self.master = master
		self.init_window()
	def init_window(self):
		global txt
		self.master.title("Calculator")
		self.pack(fill = BOTH, expand = 1)
		# Menu bar
		menu = Menu(self.master)
		self.master.config(menu=menu)
		file = Menu(menu)
		file.add_command(label='Exit', command=self.client_exit)
		menu.add_cascade(label='File', menu=file)
		
		# create buttons
		clearButton = Button(self, text="Clear", command=self.clear)
		clearButton.place(x=195, y=265)
		addButton = Button(self, text="Add", command=self.addition)
		addButton.place(x=150, y=200)
		# display window
		txt = Text(root, height=1, width=28)
		txt.place(x = 10, y = 50)
	def addition(self):
		
		a = txt.get('1.0', 'end -1c' )
		
		b = txt.get('1.0', 'end -1c' )
		
	def clear(self):
		txt.delete("1.0", END)
	def client_exit(self):
		exit()
		
		
root = Tk()

root.geometry("250x300")
app = Window(root)
root.mainloop()