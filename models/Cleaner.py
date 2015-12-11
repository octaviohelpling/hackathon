class Cleaner(db.Model):
	name = db.StringProperty()
	created = db.DateTimeProperty(auto_now_add=True)