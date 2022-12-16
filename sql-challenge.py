import sqlite3


db_name = 'files.db'
table_name = 'tbl_files'
fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')
file_ending = '.txt'

def db_create():
    conn = sqlite3.connect(db_name)
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS {}( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_filename STRING, \
            )".format(table_name))
            # does string need to be text?



def filter_data(fileList):
    filtered = [f for f in fileList if fileList.endswith(file_ending)]
    for f in filtered:
        print(f, '\n')
    return (filtered)


    # with conn:
    #     cur = conn.cursor()
    #     cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?,?,?)", ("Bill", "Jones", "bjones@aol.com"))
    #     conn.commit()
    # conn.close()



def insert_data(filtered, conn, cur):
    with conn:
        for file in filtered:
            cur.execute("INSERT INTO tbl_persons(col_filename) VALUES (?)", (file))
        conn.commit()

def close_conn(conn):
    conn.close()


if __name__ == "__main__":
    (conn, cur) = db_create()
    filtered = filter_data(fileList)
    insert_data(filtered, conn, cur)
    close_conn(conn)

