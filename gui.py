import tkinter as tk
from tkinter import ttk, messagebox, Label, Frame

class Finance_App:

	def __init__(self, root):
		self.root = root
		self.root.title ("Finance App")
		self.root.geometry('1300x800')
		self.root.maxsize(1500,900)
		self.root.config(bg='khaki')

if __name__ == '__main__':
	root = tk.Tk()
	app = Finance_App(root)
	# root.protocol('WM_DELETE_WINDOW', app.confirm_exit)
	root.mainloop()