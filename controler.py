import sqlite3 as sql 

def createDB():
    conn = sql.connect("streamers.db")
    conn.commit()
    conn.close()
    
def createTable():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE STREAMERS (
            name text,
            followers integer,
            subs integer
        )"""
    )
    conn.commit()
    conn.close()
    
def insertRow(nombre, followers, subs):
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO streamers Values ('{nombre}',{followers},{subs} )"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()
    
def readRows():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f" SELECT * FROM streamers"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)
    
def insertRows(streamerList):
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO streamers Values (?,?,?)"
    cursor.executemany(instruccion, streamerList)
    conn.commit()
    conn.close()
    
def readOrdered(field):
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f" SELECT * FROM streamers ORDER BY {field} DESC"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)
    
def search():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f" SELECT * FROM streamers WHERE name='ibsai'"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)
    
def updateFields():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f" UPDATE streamers SET followers = 12999 where name like 'ibsai'"
    cursor.execute(instruccion)

    conn.commit()
    conn.close()

    
    
if __name__ == '__main__':
    #createDB()
    #createTable()
    #insertRow("ibsai",7000,25)
    #readRows()
    streamers = [
        ("Elx",40,50),
        ("El2",44,30),
        ("rtx",430,5)
    ]
    #insertRows(streamers)
    #readOrdered("subs")
    #search()
    updateFields()