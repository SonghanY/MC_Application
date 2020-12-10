"""
A program that stores this book information:
Title, Author 
Year, ISBN

User can:

View all records
Search an entry
Add entry
Update entry
Delete
Close
"""
from tkinter import *
import backend

def get_selected_row(event):     # 这个函数也被 list1.bind()方法执行，即使在delete_command()函数中没有传入参数给event，也不能删除它
    global selected_tuple
    try:
        index = list1.curselection()[0]    # 在listbox中选中的书的序号，返回这个id给 delete_command()
        selected_tuple = list1.get(index)     # 在listbox中选中的书的信息
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])    # title
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])    # author
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])    # year
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])    # isbn
    except IndexError:  # Since the listbox is empty, list1.curselection() will be an empty list with no items. Trying to access the first item on the list with [0] will throw an error, because there is no first item in the list. 
        pass

def view_command():
    list1.delete(0, END)    # 0 end ensure that the you are deleting everything from the index of zero, to the last row.
    for row in backend.view():
        list1.insert(END, row)      # END row 让每一个新row 添加在 listbox末尾

def search_command():
    list1.delete(0, END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row)

def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    # 希望当我们点击add entry添加新书后，新书的信息就直接显示在listbox中 
    list1.delete(0, END)    
    list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())

def close_command():
    pass

window=Tk()

window.wm_title("BookStore")    # 定义窗口的title

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

title_text = StringVar()    # 用户输入的spatial data type
e1 = Entry(window, textvariable=title_text)   # entry
e1.grid(row=0,column=1)

author_text = StringVar()  
e2 = Entry(window, textvariable=author_text)   # entry
e2.grid(row=0,column=3)

year_text = StringVar()  
e3 = Entry(window, textvariable=year_text)   # entry
e3.grid(row=1,column=1)

isbn_text = StringVar()  
e4 = Entry(window, textvariable=isbn_text)   # entry
e4.grid(row=1,column=3)

list1=Listbox(window, height=6, width=35)   # Listbox
list1.grid(row=2,column=0, rowspan=6, columnspan=2)    # 添加行宽、列宽

sb1=Scrollbar(window)   # 滑动条
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

b1=Button(window, text="View all", width=12, command=view_command)
b1.grid(row=2, column=3)

b2=Button(window, text="Search entry", width=12, command=search_command)
b2.grid(row=3, column=3)

b3=Button(window, text="Add entry", width=12, command=add_command)
b3.grid(row=4, column=3)

b4=Button(window, text="Update", width=12, command=update_command)
b4.grid(row=5, column=3)

b5=Button(window, text="Delete", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6=Button(window, text="Close", width=12, command=window.destroy)   # 关闭窗口
b6.grid(row=7, column=3)

window.mainloop()
