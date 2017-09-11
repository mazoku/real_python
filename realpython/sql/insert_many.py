# INSERT Command

# import the sqlite3 library
import sqlite3

# create the connection object
with sqlite3.connect('new.db') as conn:
    # get a cursos object used to execute SQL commands
    cursor = conn.cursor()

    try:
        # insert multiple records using a tuple
        cities = [('Boston', 'MA', 600000),
                  ('Chicago', 'IL', 2700000),
                  ('Houston', 'TX', 2100000),
                  ('Philadelphia', 'PA', 1500000),
                  ('San	Antonio', 'TX', 1400000),
                  ('San	Diego', 'CA', 130000),
                  ('Dallas', 'TX', 1200000),
                  ('San	Jose', 'CA', 900000),
                  ('Jacksonville', 'FL', 800000),
                  ('Indianapolis', 'IN', 800000),
                  ('Austin', 'TX', 800000),
                  ('Detroit', 'MI', 700000)]
        cursor.executemany("INSERT INTO population VALUES(?, ?, ?)", cities)
    except sqlite3.OperationalError:
        print("Opps! Something went wrong. Try again. ")
