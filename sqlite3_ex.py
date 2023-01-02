import sqlite3

###### Create database in file location ######
# connection = sqlite3.connect("C:\GitHub\Python-Projects\\test_database.db")
# c = connection.cursor()
# c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")
# c.execute("INSERT INTO People VALUES('Ron', 'Obvious', 42)")
# connection.commit()


###### Create database in RAM ######
# connection_ram = sqlite3.connect(":memory:")
# c_ram = connection_ram.cursor()
# c_ram.execute("DROP TABLE IF EXISTS People")
# connection_ram.close()

###### Create database using "with" keyword ######
# with sqlite3.connect("test_db_with.db") as connection3:
#     # perform SQL ops here
#     # no need for commit command, they're automatically saved when connected is closed
#     # (you'll need to commi if you want to see result before closing connection)
#     pass



###### Use SQL script ######
# with sqlite3.connect('test_db_script.db') as connection:
#     c = connection.cursor()
#     c.executescript("""DROP TABLE IF EXISTS People;
#                     CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT);
#                     INSERT INTO People VALUES('Ron', 'Obvious', '42');
#                     """)
#     peopleValues = (('Luigi', 'Vercotti', 43), ('Arthur', 'Belling', 28))
#     c.executemany("INSERT INTO People VALUES(?, ?, ?)", peopleValues)


###### From user data ######
# # get personal data from user
# firstName = input("Enter your first name: ")
# lastName = input("Enter your last name: ")
# age = int(input("Enter your age: "))
# personData = (firstName, lastName, age)

# # execute insert statement for supplied person data
# with sqlite3.connect('test_db_user.db') as connection:
#     c = connection.cursor()
#     c.execute("INSERT INTO People VALUES(?, ?, ?)", personData)
#     c.execute("UPDATE People SET Age = WHERE FirstName=? AND LastName=?",
#         (45, 'Luigi', 'Vercotti'))


###### Retrieve ######
peopleValues = (('Ron', 'Obvious', 42), ('Luigi', 'Vercotti', 43), ('Arthur', 'Belling', 28))
with sqlite3.connect('test_db_retrieve.db') as connection:
    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS People")
    c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")
    c.executemany("INSERT INTO People VALUES(?, ?, ?)", peopleValues)

    # seelct all first and last names from people over 30
    c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")
    for row in c.fetchall():
        print(row)


    c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")
    while True:
        row = c.fetchone()
        if row is None:
            break
        print(row)
        