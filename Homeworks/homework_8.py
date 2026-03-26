import sqlite3

def get_books_by_author(author):
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE author = ? ORDER BY title ASC", (author,))
    books = cursor.fetchall()
    conn.close()
    return books

author_name = "Александр Пушкин"
books_list = get_books_by_author(author_name)
for book in books_list:
    print(book)