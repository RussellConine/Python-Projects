import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
import datetime

class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self)
        # set title of GUI window
        self.master.title("File Transfer")
    
        # Creates button to select files from source directory
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)

        # Position source button in GUI using grid
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))
        
        # Creates entry for source directory selection
        self.source_dir = Entry(width=75)
        # positions entry in GUI using tkinter grid
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30, 0))

        # Creates button to select destination of files from destination directory
        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        # Positions destination button in GUI usng grid
        self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15,10))

        # Creates entry for destination directory selection
        self.destination_dir = Entry(width=75)
        # Positions entry in GUI using Grid
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20,10), pady=(15,10))

        self.transfer_btn = Button(text = "Transfer Files", width=20, command=self.transferFiles)
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0, 15))

        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))

    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        # clear out the content that is inserted in the Entry widget
        self.source_dir.delete(0, END)
        self.source_dir.insert(0, selectSourceDir)

    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()
        # clear out the content that is inserted in the Entry widget
        self.destination_dir.delete(0, END)
        self.destination_dir.insert(0,selectDestDir)

    def transferFiles(self):
        # get source directory
        source = self.source_dir.get()
        destination = self.destination_dir.get()
        source_files = os.listdir(source)
        # create datetime object for current time
        current_time = datetime.datetime.now()
        # for all files in source directory
        for i in source_files:
            # create absolute filepath for each file
            source_filepath = source + "/" + i
            # create unix timestamp of when each file was last modified
            last_modified_timestamp = os.path.getmtime(source_filepath)
            # convert unix timestamp to datettime object
            last_modified = datetime.datetime.fromtimestamp(last_modified_timestamp)
            # if the file's last modified time is greater than (more recent than) 24 hours ago,
            # then move the file from source to destination
            if last_modified > current_time - datetime.timedelta(hours=24):
                shutil.move(source_filepath, destination)
                print(i + ' was transferred')

    # close window and all widgets when program is exited
    def exit_program(self):
        root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

