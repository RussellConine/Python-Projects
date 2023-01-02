from tkinter import *

win = Tk()
lb = Listbox(win, height = 3)
lb.pack()
lb.insert(END, "First Entry")
lb.insert(END, "Second Entry")
lb.insert(END, "Third Entry")
lb.insert(END, "Fourth Entry")
sb = Scrollbar(win, orient = VERTICAL)
sb.pack(side=LEFT, fill=Y)
sb.configure(command=lb.yview)
lb.configure(yscrollcommand=sb.set)

print(lb.curselection())
win.mainloop()