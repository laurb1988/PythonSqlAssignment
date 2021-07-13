import sqlite3

conn = sqlite3.connect("BookStore.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE "Books" (
	"ID"	INTEGER NOT NULL UNIQUE,
	"Title"	TEXT NOT NULL,
	"Year"	INTEGER NOT NULL,
	PRIMARY KEY("ID")
);
""")
conn.commit()

def UserValues():
    books = {}
    books['ID'] = int(input("Enter book ID: "))
    books['Title'] = str(input("Enter book name: "))
    books['Year'] = int(input("Enter book year: "))
    return(books)

books = UserValues()
cursor.execute("INSERT INTO Books VALUES (:ID, :Title, :Year)", books)
conn.commit()

cursor.execute("SELECT * FROM Books;")
all_results = cursor.fetchall()
print(all_results)