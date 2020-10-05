""""
A program that stores this book information:
*Title
*Author
*Year
*ISBN

User can:

View all records
Search any entry
Add entry
Update entry
Delete
Close
"""

from tkinter import *
import backend

window = Tk()
l1=Label(window, text='Title')
l1.grid(row=0, column=0)

l2=Label(window, text='Year')
l2.grid(row=1, column=0)

l3=Label(window, text='Author')
l3.grid(row=0, column=2)

l4=Label(window, text='ISBN')
l4.grid(row=1, column=2)

title_txt = StringVar()
e1 = Entry(window,textvariable=title_txt)
e1.grid(row=0, column=1)

author_txt = StringVar()
e2 = Entry(window, textvariable=author_txt)
e2.grid(row=0, column=3)

year_txt = StringVar()
e3 = Entry(window, textvariable=year_txt)
e3.grid(row=1, column=1)


isbn_txt = StringVar()
e4 = Entry(window, textvariable=isbn_txt)
e4.grid(row=1, column=3)

list1=Listbox(window, height = 6, width =  35)
list1.grid(row = 2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1 = Button(window, text='View all', width=12)
b1.grid(row=2, column=3)


b1 = Button(window, text='Search Entry', width=12)
b1.grid(row=3, column=3)


b1 = Button(window, text='Add entry', width=12)
b1.grid(row=4, column=3)

b1 = Button(window, text='Update selected', width=12)
b1.grid(row=5, column=3)


b1 = Button(window, text='Delete selected', width=12)
b1.grid(row=6, column=3)


b1 = Button(window, text='Close', width=12)
b1.grid(row=7, column=3)



b1 = Button(window, text='View all', width=12)
b1.grid(row=2, column=3)

"""
This is an example of Google style.

Args:
    param1: This is the first param.
    param2: This is a second param.

Returns:
    This is a description of what is returned.

Raises:
    KeyError: Raises an exception.
"""




window.mainloop()
