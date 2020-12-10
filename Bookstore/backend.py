import sqlite3

def connect():
    conn = sqlite3.connect("books.db")  # 连接数据库
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn = sqlite3.connect("books.db")  # 连接数据库
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("books.db")  # 连接数据库
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()   # return my slection as a tuple, grab that selection and put that in the list box
    conn.close()    # 因为我们不需要改变数据库，所以不需要conn.commit()
    return rows     # my data store in 'rows' variable

def search(title="", author="", year="", isbn=""):  # 因为可能只输入一个变量，所以添加 empty string as default values
    conn = sqlite3.connect("books.db")  # 连接数据库
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("books.db")  # 连接数据库
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))   # 别忘了这里的逗号
    conn.commit()
    conn.close()

def update(id, title, author, year, isbn):
    conn = sqlite3.connect("books.db")  # 连接数据库
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title,author,year,isbn,id))
    conn.commit()
    conn.close()

connect()
#insert("The Sun", "John Smith", 1918, 913123132)
#delete(3)
#update(4,"The moon","John Smooth",1917,99999)
print(view())
print(search(author="John Smith"))
