import tkinter as tk
from tkinter import ttk, messagebox, Label, Frame, Button, filedialog
import os

bank_options = ['Regions', 'Chase']
expense_type = ['Rent','Utilities','Groceries','Dining Out','Entertainment','Miscellaneous']

class Finance_App:

	def __init__(self, root):
		self.root = root
		self.root.title ("Finance App")
		self.root.geometry('1300x800')
		self.root.maxsize(1500,900)
		self.root.config(bg='khaki')
		self.create_widgets()

	def create_widgets(self):
		left_frame = Frame(self.root,width=200,height=400,bg='red')
		left_frame.grid(row=0,column=0,padx=10,pady=5)

		bank_label = Label(left_frame,text='Choose Bank')
		bank_label.grid(row=0,column=0,padx=5,pady=5)

		bank_var = tk.StringVar()
		bank_combo = ttk.Combobox(left_frame,textvariable=bank_var,state='readonly',values=bank_options)
		bank_combo.grid(row=0,column=1,padx=5,pady=5)

		upload_button = Button(left_frame,text='Upload Statement',command=self.browse_file)
		upload_button.grid(row=1,column=0,padx=5,pady=5)

	def browse_file(self):
		file_path = filedialog.askopenfilename(filetypes=[('CSV files','*.csv')])
		

if __name__ == '__main__':
	root = tk.Tk()
	app = Finance_App(root)

	# root.protocol('WM_DELETE_WINDOW', app.confirm_exit)
	root.mainloop()