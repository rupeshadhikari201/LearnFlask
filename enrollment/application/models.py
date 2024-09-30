from application import db

class Users(db.Document):
    user_id = db.IntField(unique=True)
    first_name= db.StringField(max_len=50)
    last_name= db.StringField(max_len=50)
    email= db.StringField(max_len=30)
    password= db.StringField(max_len=30)
    
class Courses(db.Document):
    course_id = db.IntField(max_len=10,unique=True) 
    title = db.StringField(max_len=50)
    description = db.StringField(max_len=100)
    credits = db.IntField(max_len=2)
    term = db.StringField(max_len=50)
    
    
class Enrollment(db.Document):
    user_id = db.IntField()
    course_id = db.StringField()
     