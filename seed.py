from application import db
from application.models import Quote

db.drop_all()
print("Dropping database")
db.create_all()
print("Creating database")

print("Seeding database")
entry1 = Quote(quote='Decentralize')

entry2 = Quote(quote='Distraction is the enemy of vision')

entry3 = Quote(quote='Believe in your flyness...conquer your shyness.')


db.session.add_all([entry1, entry2, entry3])

db.session.commit()

