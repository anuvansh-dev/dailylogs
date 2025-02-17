"""Library Management System utilizing SQLite db
-This system can perform CRUD opeartions on vbooks in the library
"""

import sqlite3


def create_connection(db_name):
    """Establishe connection to the SQLite database."""
    conn = sqlite3.connect(db_name)
    return conn


def create_books_table(conn):
    """Create 'books' table in the db."""
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR(60) NOT NULL,
            author VARCHAR(25) NOT NULL
                   
        );
    ''')
    conn.commit()


def add_book(conn, title, author):
    """Insert a new book into the books table."""
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO books (title, author)
        VALUES (?, ?);
    ''', (title, author))
    conn.commit()
    print(f"Book '{title}' by author {author} is added successfully!")


def view_books(conn):
    """Fetches all records from the books table."""
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books;')
    books = cursor.fetchall()

    if books:
        print("Books in the Library:")
        for book in books:
            print(f"ID: {book[0]}\nTitle: {book[1]}\nAuthor: {book[2]}")
    else:
        print("No Books are available in the Library!")


def update_book(conn, book_id, title=None, author=None):
    """Updates book details in the Library."""
    cursor = conn.cursor()
    
    if title:
        cursor.execute('UPDATE books SET title = ? WHERE id = ?;', (title, book_id))
    
    if author:
        cursor.execute('UPDATE books SET author = ? WHERE id = ?;', (author, book_id))

    conn.commit()
    print(f"Book ID {book_id} is updated successfully!")


def delete_book(conn, book_id):
    """Deletes book from the Library."""
    cursor = conn.cursor()
    cursor.execute('DELETE FROM books WHERE id = ?;', (book_id,))
    conn.commit()
    print(f"Book ID {book_id} is deleted successfully!")


def main():
    
    #main interface for the system
    conn = create_connection("library.db")
    create_books_table(conn)

    while True:
        print("\nLibrary Management System")
        print("1. Add a book")
        print("2. View all books")
        print("3. Update a book")
        print("4. Delete a book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")

            add_book(conn, title, author)

        elif choice == '2':
            view_books(conn)

        elif choice == '3':
            book_id = int(input("Enter book ID to update: "))
            title = input("Enter book title (or press enter to skip): ")
            author = input("Enter athor name (or press enter to skip): ")

            update_book(conn, book_id, title, author)

        elif choice == '4':
            book_id = int(input("Enter book id to delete: "))

            delete_book(conn, book_id)

        elif choice == '5':
            print("Exiting the system.")
            conn.close()
            break

        else:
            print("Invalid choice, please enter a valid option.")


if __name__ == "__main__":
    main()