from Lessons.database import (
    create_tables,
)
import sqlite3

from Lessons.database import add_student

connection = sqlite3.connect('database.db')
create_tables(connection)
add_student(connection,
            "ibr", 20, "Bishkek")



