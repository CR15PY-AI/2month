import sqlite3


class Library:
    def __init__(self, db_name = "library.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()
    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS library(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL
        )
    """)
    
    def add_book(self, book):
        self.cursor.execute("INSERT INTO library (title, author) VALUES (?,?)", (book.title, book.author))
        self.connection.commit()

    def delete_book_by_id(self, book_id):
        self.cursor.execute("DELETE FROM library WHERE id = ?", (book_id))
        self.connection.commit()
        print(f"Книга с номером {book_id} была удалена")

    def list_books(self):
        self.cursor.execute("SELECT * FROM library")
        books = self.cursor.fetchall()
        print(books)
        