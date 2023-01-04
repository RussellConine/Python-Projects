import tkinter as tk
from tkinter import *
import tkinter.filedialog

class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self)
        # set title of GUI window
        self.master.title("File Transfer")
    
        # Creates button to select files from source directory
        self.sourceDir_btn = Button(text="Select Source", width=20)

        # Position source button in GUI using grid
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))
        
        # Creates entry for source directory selection
        self.source_dir = Entry(width=75)
        # positions entry in GUI using tkinter grid
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30, 0))

        # Creates button to select destination of files from destination directory
        self.destDir_btn = Button(text="Select Destination", width=20)
        # Positions destination button in GUI usng grid
        self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15,10))

        # Creates entry for destination directory selection
        self.destination_dir = Entry(width=75)
        # Positions entry in GUI using Grid
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20,10), pady=(15,10))

        def sourceDir(self):
            selectSourceDir = tkinter.filedialog.askdirectory()
            # clear out the content that is inserted in the Entry widget
            



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

