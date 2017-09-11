# SQLite Functions

import sqlite3

with sqlite3.connect('new.db') as connections:
    c = connections.cursor()

    # create a dictionary of sql queries
    sql = {'average': "SELECT avg(population) FROM population",
           'maximum': "SELECT max(population) FROM population",
           'minimum': "SELECT min(population) FROM population",
           'sum': "SELECT sum(population) FROM population",
           'count': "SELECT count(population) FROM population"}

    # run each sql query item in the dictionary
    for keys, values in sql.items():
        # run sql
        c.execute(values)

        # fetchone() retireves one record from the query
        result = c.fetchone()

        # output the result to screen
        print(keys + ':', result[0])