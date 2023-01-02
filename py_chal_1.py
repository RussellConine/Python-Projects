import sqlite3

###### Create database in RAM ######
with sqlite3.connect(":memory:") as connection: 
    c= connection.cursor()
    c.executescript("""DROP TABLE IF EXISTS Roster;
                    CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT);
                    """)
    data_values = (("Jean-Baptiste Zorg", "Human", 122),
                    ("Korben Dallas", "Meat Popsicle", 100),
                    ("Ak'not", "Mangalore", -5))
    c.executemany("INSERT INTO Roster VALUES (?, ?, ?)", data_values)
    c.execute("UPDATE Roster SET Species=? WHERE Name=?",('Human', 'Korben Dallas'))

    # select all first and last names from people over 30
    c.execute("SELECT Name, IQ FROM Roster WHERE Species=?", ('Human',))
    for row in c.fetchall():
        print(row)
