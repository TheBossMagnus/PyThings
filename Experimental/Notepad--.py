# Importing Required libraries & Modules
from tkinter import Label, Scrollbar, Text, END, RIGHT, VERTICAL, Y, BOTH, GROOVE, BOTTOM, Tk
from tkinter import messagebox
from tkinter import filedialog
import sys


# Defining TextEditor Class
class TextEditor:


  def __init__(self,root):
    self.root = root
    self.root.title("Notepad--")
    self.root.geometry("1200x700+200+150")
    self.filename = None

    # Creating Statusbar
    self.statusbar = Label(self.root, text="Ctrl+N : New File | Ctrl+O : Open File | Ctrl+S : Save File | Ctrl+A : Save As File | Ctrl+E : Exit | Ctrl+X : Cut | Ctrl+C : Copy | Ctrl+V : Paste", font=("times new roman",15,"bold"),bd=2,relief=GROOVE)
    # Packing status bar to root window
    self.statusbar.pack(side=BOTTOM,fill=BOTH)


    # Creating Scrollbar
    scrol_y = Scrollbar(self.root,orient=VERTICAL)
    # Creating Text Area
    self.txtarea = Text(self.root,yscrollcommand=scrol_y.set,font=("times new roman",15,"bold"),state="normal",relief=GROOVE)
    # Packing scrollbar to root window
    scrol_y.pack(side=RIGHT,fill=Y)
    # Adding Scrollbar to text area
    scrol_y.config(command=self.txtarea.yview)
    # Packing Text Area to root window
    self.txtarea.pack(fill=BOTH,expand=1)

    # Calling shortcuts funtion
    self.shortcuts()


  # Defining New file Function
  def newfile(self, outfile):
    # Clearing the Text Area
    self.txtarea.delete("1.0",END)
    # Updating filename as None
    self.filename = None


  # Defining Open File Funtion
  def openfile(self, outfile):
    # Asking for file to open
    self.filename = filedialog.askopenfilename(title = "Select file",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))
    # checking if filename not none
    if self.filename:
      # opening file in readmode
      with open(self.filename,"r",encoding="utf-8") as infile:
      # Clearing text area
        self.txtarea.delete("1.0",END)
        # Inserting data Line by line into text area
        for line in infile:
          self.txtarea.insert(END,line)
        # Closing the file  
        infile.close()


  # Defining Save File Funtion
  def savefile(self, outfile):
    # Exception handling
    # checking if filename not none
    if self.filename:
      # Reading the data from text area
      data = self.txtarea.get("1.0",END)
      # opening File in write mode
      with open(self.filename,"w",encoding="utf-8") as outfile:
        # Writing Data into file
        outfile.write(data)
        # Closing File
        outfile.close()
    else:
        self.saveasfile()

  # Defining Save As File Funtion
  def saveasfile(self, outfile):
    # Exception handling
    # Asking for file name and type to save
    untitledfile = filedialog.asksaveasfilename(title = "Save file As",defaultextension=".txt",initialfile = "Untitled.txt",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))
    # Reading the data from text area
    data = self.txtarea.get("1.0",END)
    # opening File in write mode
    with open(untitledfile,"w", encoding="utf-8") as outfile:
      # Writing Data into file
      outfile.write(data)
      # Closing File
      outfile.close()
      # Updating filename as Untitled
      self.filename = untitledfile


  # Defining Exit Funtion
  def exit(self, op):
    op = messagebox.askyesno("WARNING","Your Unsaved Data May be Lost!!")
    if op>0:
      sys.exit()
    else:
      return

  # Defining Cut Funtion
  def cut(self):
    self.txtarea.event_generate("<<Cut>>")

  # Defining Copy Funtion
  def copy(self):
          self.txtarea.event_generate("<<Copy>>")

  # Defining Paste Funtion
  def paste(self):
    self.txtarea.event_generate("<<Paste>>")


  # Defining shortcuts Funtion
  def shortcuts(self):
    # Binding Ctrl+n to newfile funtion
    self.txtarea.bind("<Control-n>",self.newfile)
    # Binding Ctrl+o to openfile funtion
    self.txtarea.bind("<Control-o>",self.openfile)
    # Binding Ctrl+s to savefile funtion
    self.txtarea.bind("<Control-s>",self.savefile)
    # Binding Ctrl+a to saveasfile funtion
    self.txtarea.bind("<Control-a>",self.saveasfile)
    # Binding Ctrl+e to exit funtion
    self.txtarea.bind("<Control-e>",self.exit)
    # Binding Ctrl+x to cut funtion
    self.txtarea.bind("<Control-x>",self.cut)
    # Binding Ctrl+c to copy funtion
    self.txtarea.bind("<Control-c>",self.copy)
    # Binding Ctrl+v to paste funtion
    self.txtarea.bind("<Control-v>",self.paste)

# Creating TK Container
root = Tk()
# Passing Root to TextEditor Class
TextEditor(root)
# Root Window Looping
root.mainloop()