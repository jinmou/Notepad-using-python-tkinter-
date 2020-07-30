"""
Author - Krish Bista
Date - 29 July 2020
Purpose - Notepad
"""

import tkinter
from tkinter import filedialog
import os
import tkinter.messagebox


class Notepad(tkinter.Tk):
    
    # Creating a constructer
    
    def __init__(self):
        super().__init__()
        

        # Setting the basic window of Notepad

        self.geometry("600x700")
        self.title("Untitled - Notepad")
        self.wm_iconbitmap("notepad.png.ico")
        self.file = None

        # Creating scroll bar and text area

        sbar = tkinter.Scrollbar(self)
        sbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        self.textArea = tkinter.Text(self, bg="white", font="lucida 13",     
                            yscrollcommand=sbar.set)

        self.textArea.pack(fill=tkinter.BOTH, expand=True)
        sbar.config(command=self.textArea.yview)

        # End scroll bar and text area


        # Creating menu bar

        menuBar = tkinter.Menu(self)
        self.config(menu=menuBar)

        # End menu bar


        # Creating file menu

        fileMenu = tkinter.Menu(menuBar, tearoff=0)
        fileMenu.add_command(label="New", command=self.new_file, accelerator="Ctrl + N")
        fileMenu.add_command(label="Open", command=self.open_file, accelerator="Ctrl + O")
        fileMenu.add_command(label="Save", command=self.save_file, accelerator="Ctrl + S")
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self.exit_np, activebackground="red2")

        menuBar.add_cascade(label="File", menu=fileMenu)

        # End file menu


        # Binding shortcut keys for file menu

        self.bind("<Control-n>", self.new_file)
        self.bind("<Control-o>", self.open_file)
        self.bind("<Control-s>", self.save_file)

        # End shortcut keys for file menu 


        # Creating edit menu

        editMenu = tkinter.Menu(menuBar, tearoff=0)
        editMenu.add_command(label="Copy", command=self.copy, accelerator="Ctrl + C")
        editMenu.add_command(label="Paste", command=self.paste, accelerator="Ctrl + V")
        editMenu.add_command(label="Cut", command=self.cut, accelerator="Ctrl + X")
        editMenu.add_command(label="Select All", command=self.select_all, accelerator="Ctrl + A")

        menuBar.add_cascade(label="Edit", menu=editMenu)

        # End edit menu


        # Help menu

        helpMenu = tkinter.Menu(menuBar, tearoff=0)
        helpMenu.add_command(label="About", command=self.about)
        menuBar.add_cascade(label="Help", menu=helpMenu)

        # End help menu


    # Functions for file menu

    def new_file(self, event):
        """
        This function creates a new file
        """
        user = tkinter.messagebox.askyesno(title="Notepad", 
                message="Are you sure want to continue all unsaved changes will be gone??")
        if user:
            self.file = None
            self.title("Untitled - Notepad")
            self.textArea.delete(1.0, tkinter.END)


    def open_file(self, event):
        """
        This function opens a existing file
        """

        user = tkinter.messagebox.askyesno(title="Notepad", 
                    message="Are you sure want to open another file \n All unsaved changes will be gone ?")
        
        if user:
        
            self.file = filedialog.askopenfilename(defaultextension=".txt", 
                                                    filetypes=[("All Files", "*.*"), ("Text documents", "*.txt")])           

            if self.file == "":
                self.file = None

            else:
                self.title(os.path.basename(self.file) + " - Notepad")
                self.textArea.delete(1.0, tkinter.END)
                f = open(self.file, "r")
                self.textArea.insert(1.0, f.read())
                f.close()


    def save_file(self, event):
        """
        This function saves a file
        """

        if self.file==None:
            self.file = filedialog.asksaveasfilename(defaultextension=".txt", 
                                filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])       

            if self.file == "":
                self.file = None
            else:
                # Save as new file
                self.title(os.path.basename(self.file) + " - Notepad")
                f = open(self.file, "w")
                f.write(self.textArea.get(1.0, tkinter.END))
                f.close()
                 
        else:
            # Update existing file
            f = open(self.file, "w")
            f.write(self.textArea.get(1.0, tkinter.END))
            f.close()
                 
            
    def exit_np(self):
        """
        This function closes the program
        """
        self.destroy()
    
    # End functions for file menu

    
    # Functions for edit menu
   
    def copy(self):
        self.textArea.event_generate("<<Copy>>")


    def paste(self):
        self.textArea.event_generate("<<Paste>>")
    

    def cut(self):
        self.textArea.event_generate("<<Cut>>")


    def select_all(self):
        self.textArea.tag_add("sel", 1.0, tkinter.END)

    # End functions for edit menu
    

    # Functions for help menu

    def about(self):
        tkinter.messagebox.showinfo(title="Notepad", 
                message="This is a notepad created by me Krish Bista\nAnd I am very happy...xD")        

    # End functions for help menu    
    

if __name__ == "__main__":
    window = Notepad()
    window.mainloop()


