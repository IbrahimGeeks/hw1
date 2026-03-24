import sqlite3


def create_table(connection):
    connection.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        name TEXT,
        author TEXT,
        publication_year INTEGER,
        genre TEXT,
        number_of_pages INTEGER,
        number_of_copies INTEGER
    )
    """)
    connection.commit()

def insert_books(connection):
    books = [
        ("Война и мир", "Лев Толстой", 1869, "Роман", 1225, 2),
        ("Преступление и наказание", "Фёдор Достоевский", 1866, "Роман", 671, 3),
        ("Мастер и Маргарита", "Михаил Булгаков", 1967, "Фантастика", 480, 4),
        ("Евгений Онегин", "Александр Пушкин", 1833, "Поэма", 224, 5),
        ("Герой нашего времени", "Михаил Лермонтов", 1840, "Роман", 300, 2),
        ("Анна Каренина", "Лев Толстой", 1877, "Роман", 864, 3),
        ("Отцы и дети", "Иван Тургенев", 1862, "Роман", 288, 4),
        ("Доктор Живаго", "Борис Пастернак", 1957, "Роман", 592, 2),
        ("Тихий Дон", "Михаил Шолохов", 1940, "Исторический роман", 1500, 1),
        ("Обломов", "Иван Гончаров", 1859, "Роман", 576, 3)
    ]

    connection.executemany("""
    INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies)
    VALUES (?, ?, ?, ?, ?, ?)
    """, books)

    connection.commit()



if __name__ == "__main__":

    connection = sqlite3.connect("library.db")

    create_table(connection)

    insert_books(connection)

    connection.close()

    print("Таблица создана и данные успешно добавлены!")