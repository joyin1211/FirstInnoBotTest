from config import DB as db

db.connect()

db.create_tables(['User', 'Message'])

db.close()
