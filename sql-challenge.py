import sqlite3


### Global Vars List ###
db_name = 'files.db'
table_name = 'tbl_files'
fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')
file_ending = '.txt'

def db_create():
    """ Function to create database, connection, and cursor
    """
    # create database and connection
    conn = sqlite3.connect(db_name)
    with conn:
        # create cursor
        cur = conn.cursor()
        # SQL to create table, with autoincrementing primary key 
        cur.execute("CREATE TABLE IF NOT EXISTS {}( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_filename STRING \
            )".format(table_name))
    # return connection and cursor so future SQL can access the databse using same connection and cursor
    return conn, cur



def filter_data(fileList):
    """ Function to filter the filelist to only select files with chosen ending
    """
    # list comprehension to filter by chosen filetype ending
    filtered = [f for f in fileList if f.endswith(file_ending)]
    print("\nThese files will be added to the database:")
    for f in filtered:
        # print filetypes with chosen ending
        print(f)
    # return files so they can be inserted into database
    return (filtered)


def insert_data(filtered, conn, cur):
    """ Function to use existing connection and cursor to write data from filtered list into database
    """
    with conn:
        for file in filtered:
            cur.execute("INSERT INTO {}(col_filename) VALUES (?)".format(table_name), (file,))
        conn.commit()

def close_conn(conn):
    """ Function to close connection to database
    """
    conn.close()


if __name__ == "__main__":
    # create database, connection to database, and cursor, and return conenction and cursor for 
    # other functions to use
    (conn, cur) = db_create()

    # filter list by chosen file ending
    filtered = filter_data(fileList)

    # insert items from filtered list into database, using existing connection and cursor
    insert_data(filtered, conn, cur)

    # close connection to database
    close_conn(conn)

