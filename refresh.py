import sqlite3

def query_all():
    #CONNECT TO DATABASE
    conn=sqlite3.connect('bloodbank.db')
    #CREATE A CURSOR
    c=conn.cursor()
    #QUERY THE DATABASE
    c.execute("""SELECT * FROM donors""")
    items=c.fetchall()
    for i in items:
        print(i[0]+"\t"+str(i[1])+"\t"+str(i[2]))
    conn.commit()
    conn.close()

def add_one(name,age,number):
    #CONNECT TO DATABASE
    conn=sqlite3.connect('bloodbank.db')
    #CREATE A CURSOR
    c=conn.cursor()
    #Insert The record
    c.execute("INSERT INTO donors VALUES (?,?,?)",(name,age,number))
    conn.commit()
    conn.close()

def delete_one(id):
    #CONNECT TO DATABASE
    conn=sqlite3.connect('bloodbank.db')
    #CREATE A CURSOR
    c=conn.cursor()
    #Insert The record
    c.execute("DELETE FROM donors WHERE rowid=(?)",id)
    conn.commit()
    conn.close()

