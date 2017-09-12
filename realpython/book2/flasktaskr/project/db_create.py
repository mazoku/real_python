
from views import db
from models import Task
from datetime import date


# create the database and the db table
db.create_all()

# insert data
db.session.add(Task('Finish this tutorial', date(2017, 9, 12), 10, 1))
db.session.add(Task('Finish Real Python', date(2017, 9, 17), 9, 1))

# commit the changes
db.session.commit()