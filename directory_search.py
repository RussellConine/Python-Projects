import os
import tkinter
import tkinter.filedialog
import datetime


chosen_file_extension = ".txt"

def select_folder():
    """Ask for directory with files. This function returns all files in chosen directory
    """
    root = tkinter.Tk()
    root.withdraw()
    directory_path = tkinter.filedialog.askdirectory(
        initialdir=os.getcwd(), 
        title='Select Directory')
    return directory_path


def search_folder(directory_path):
    """Search chosen folder for files of selected type (selected in chosen_file_extension)
    """
    dir_list = os.listdir(directory_path)
    for file in dir_list:
        if file.endswith(chosen_file_extension):
            file_path = os.path.join(directory_path,file)
            mod_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%c')
            print("File: ", file_path, "\nLast Modified: ", mod_time, "\n")



if __name__ == "__main__":
    directory_path = select_folder()
    search_folder(directory_path)