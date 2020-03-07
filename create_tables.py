from config import DB as db
from models import User, Message
db.connect()

db.create_tables([User, Message])

db.close()
