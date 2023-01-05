import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        # Label
        self.lbl = tk.Label(self.master,text="Enter custom text or click the Default HTML page button")
        self.lbl.grid(row=0,column=0,padx=(27,0),pady=(10,5))

        # Entry box
        # create StringVar so we can access text in entrybox
        self.box_text = StringVar()
        self.custom_text_box = tk.Entry(self.master,textvariable=self.box_text)
        self.custom_text_box.grid(row=1,column=0,columnspan=3,padx=(30,40),pady=(0,0), sticky=E+W)

        # Default button
        self.btn_def = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn_def.grid(row=2, column=1, padx=(10, 10), pady=(10,10))

        # Custom Text button
        self.btn_cus = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customHTML)
        self.btn_cus.grid(row=2, column=2, padx=(10, 10), pady=(10,10))


    def defaultHTML(self):
        htmlText = "Stay tuned for our summer sale!"
        # create and open file to write html to
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        # write html to html file
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    def customHTML(self):
        htmlFile = open("index.html", "w")
        # access text in entry box by calling get method on stringvar
        htmlContent = "<html>\n<body>\n<h1>" + self.box_text.get() + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
        # set value of stringvar to empty (makes entry box blank)
        self.box_text.set("")

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()