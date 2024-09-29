from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
from flask_marshmallow import Marshmallow
import os
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from dotenv import load_dotenv
from flask_mail import Mail, Message

app  = Flask(import_name=__name__)
# print(app)
# print(__name__)


# take environment variables from .env.
load_dotenv()       


# some database configuration
basedir = os.path.abspath(os.path.dirname(__file__))
# print("basedir : ", basedir)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'planet.db')
app.config['JWT_SECRET_KEY'] = os.getenv('SECRET_KEY')


# mailtrap configuration
# app.config['MAIL_SERVER']= os.environ['MAIL_SERVER']
# app.config['MAIL_PORT'] = os.environ['MAIL_PORT']
# app.config['MAIL_USERNAME'] = os.environ['MAIL_USERNAME']
# app.config['MAIL_PASSWORD'] = os.environ['MAIL_PASSWORD']
# app.config['MAIL_USE_TLS'] = os.environ['MAIL_USE_TLS']
# app.config['MAIL_USE_SSL'] = os.environ['MAIL_USE_SSL']

# Flask-Mail Configuration settings
app.config['MAIL_SERVER'] = 'smtp.gmail.com'                # Your SMTP server
app.config['MAIL_PORT'] = 587                               # SMTP port for TLS
app.config['MAIL_USE_TLS'] = True                           # Enable TLS
app.config['MAIL_USE_SSL'] = False                          # Disable SSL if using TLS
app.config['MAIL_USERNAME'] = os.environ['MAIL_USERNAME']   # Your email
app.config['MAIL_PASSWORD'] = os.environ['MAIL_PASSWORD']  # Your email password
app.config['MAIL_DEFAULT_SENDER'] = os.environ['MAIL_USERNAME']  
app.config['MAIL_MAX_EMAILS'] = None                        # Optional: set the max number of emails per connection
app.config['MAIL_SUPPRESS_SEND'] = False                    # Disable email sending in testing
app.config['MAIL_ASCII_ATTACHMENTS'] = False                # Optional: set to True if you need ASCII-only filenames


db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)
mail = Mail(app)


@app.cli.command('db_create')
def db_create():
    db.create_all()
    print("Database Created.")


@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print("Databse Dropped")


@app.cli.command('db_seed')
def db_seed():
    
    mercury = Planet(planet_name='Mercury',
                     planet_type ='Class D',
                     home_star = 'Sol',
                     mass=3.258e23,
                     radius=1516,
                     distance=35.98e6)
    
    venus = Planet(planet_name='Venus',
                     planet_type ='Class K',
                     home_star = 'Sol',
                     mass=4.867e24,
                     radius=3760,
                     distance=67.24e6)
    
    earth = Planet(planet_name='Earth',
                     planet_type ='Class M',
                     home_star = 'Sol',
                     mass=5.972e24,
                     radius=3959,
                     distance=92.96e6)
    
    db.session.add(mercury)
    db.session.add(venus)
    db.session.add(earth)
    
    test_user  = User(first_name="Rupesh",
                      last_name="Yadav",
                      email='21bcs11201@gmail.com',
                      password="Hello@123")

    db.session.add(test_user)
    db.session.commit()
    print("Databse Seeded.")


@app.route('/')
def home():
    return "Hello, World"


@app.route('/super_simple')
def super_simple():
    return jsonify(message='Welcome to Planetary API'),200


@app.route('/not_found')
def not_found():
    return jsonify(message='Sorry, URL not Found'),404


# URL Parameters
app.route('/url_parameters')
def url_parameter():
    name = request.args.get('name')
    age = int(request.args.get('age'))
    print(name, age)
    if age < 18:
        return jsonify(message="Sorry, " + name + " Your are not eligible." ),401
    else:
        return jsonify(message="Yayy, " + name + " Your are  eligible." ),200
    
    
# URL Variables and Conversion Filters
app.route('/url_variables/<string:name>/<int:age>')
def url_variables(name, age):
    if age < 18:
        return jsonify(message="Sorry, " + name + " Your are not eligible." ),401
    else:
        return jsonify(message="Yayy, " + name + " Your are  eligible." ),200


#Get all the planets for the database
@app.route('/planets', methods=['GET'])
def get_planets():
    planets = Planet.query.all()
    serialized_data = planets_schema.dump(planets)
    return jsonify(serialized_data)


# Register User
@app.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    print(email)
    test = User.query.filter_by(email=email).first()
    print(test)
    if test:
        return jsonify(message='Email already exists'), 409
    else:
        first_name = request.form['first_name'] 
        last_name = request.form['last_name'] 
        password = request.form['password']
        new_user = User(first_name=first_name, last_name=last_name, email=email,password=password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify(message="User Created!"), 201
        

# Login User
@app.route('/login', methods=['POST'])
def login():
    if request.is_json:
        email = request.json.get('email')
        password = request.json.get('password')
    else:
        email = request.form['email']
        password = request.form['password']
    
    user = User.query.filter_by(email=email, password=password).first()
    if not user:
        return jsonify(message="Bad Email or password!!!"), 401
    else:
        access_token = create_access_token(identity=email)
        return jsonify(message = "Login Sucessful", access_token = access_token), 200
        
        
#Get all the planets for the database
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    serialized_data = users_schema.dump(users)
    return jsonify(serialized_data)


# Retrive password to mail
@app.route('/retrive_password/<string:email>/')
def retrive_password(email: str):
    user = User.query.filter_by(email=email).first()
    if user:
        # Create a message object
        msg = Message(
            subject="Hello from Flask-Mail",
            body="Your Planetary API password is : "+ user.password,
            sender=app.config['MAIL_DEFAULT_SENDER'],
            recipients=[email])
        
        mail.send(msg)
        return jsonify(message="Message sent to " + email)
    else:
        return jsonify(message="That email doesn't exists.")


# CRUD
# 1. GET all planet details by id
@app.route('/planet_details/<int:planet_id>', methods=['GET'])
def planet_details(planet_id : int):
    planet = Planet.query.filter_by(planet_id=planet_id).first()
    if planet:
        planet  = Planet.query.filter_by(planet_id=planet_id).first()
        result = planet_schema.dump(planet)
        return jsonify(result), 200
    else:
        return jsonify(messgae="The planed with id : "+ str(planet_id) + " doesn't exists!"), 404


# 2. Add Planet with post and Secure the Endpoint
@app.route('/add_planet', methods=['POST'])
@jwt_required()
def add_planet():
    planet_name = request.json['planet_name']
    planet = Planet.query.filter_by(planet_name=planet_name).first()
    if planet:
        return jsonify(message="The planet " + planet_name + " already exists."),409
    else:
        planet_type = request.json['planet_type']
        home_star = request.json['home_star']
        mass = float(request.json['mass'])
        radius = float(request.json['radius'])
        distance = float(request.json['distance'])
        
        new_planet = Planet(planet_name=planet_name,planet_type=planet_type, home_star=home_star, mass=mass, distance=distance,radius=radius)
        db.session.add(new_planet)
        db.session.commit()
        return jsonify(message="Planet " + planet_name + " added to the database." ), 201
   
   
# 3. Update the planet_details using Put
@app.route('/update_planet', methods=['PUT'])
@jwt_required()
def update_planet():
    planet_id = request.json['planet_id']
    planet = Planet.query.filter_by(planet_id=planet_id).first()
    print('planet is : ', planet)
    print('planet type is : ', type(planet))
    if planet:
        print(planet.planet_name)
        planet.planet_name = request.json['planet_name']
        planet.planet_type = request.json['planet_type']
        planet.home_star = request.json['home_star']
        planet.mass = float(request.json['mass'])
        planet.radius = float(request.json['radius'])
        planet.distance = float(request.json['distance'])
        db.session.commit()
        return jsonify(message="The planet is now updated"), 201
    else:
        return jsonify(message="The planet with id : " + str(planet_id ) + " doesn't exists."), 404
 

# 4. Delete the planet from the database
@app.route('/delete_planet/<int:planet_id>', methods=['DELETE'])
@jwt_required()
def delete_planet(planet_id : int):
    planet = Planet.query.filter_by(planet_id=planet_id).first()
    if planet:
        # print(planet.planet_name)
        db.session.delete(planet)
        db.session.commit()
        return jsonify(message="The planet is now deleted."),200
    else:
        return jsonify(message= "THe planet with planet id : " + str(planet_id) + " doesn't exists."), 404
        
# Models for the databse
class User(db.Model):
    __tablename__='users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    

class Planet(db.Model):
    __tablename__='planets'
    planet_id = Column(Integer, primary_key=True)
    planet_name = Column(String)
    planet_type = Column(String)
    home_star = Column(String)
    mass = Column(Float)
    radius = Column(Float)
    distance = Column(Float)


# User Schema
class UserSchema(ma.Schema):
    class Meta:
        fields = ('first_name', 'last_name','email','password')


# Planet Schema
class PlanetSchema(ma.Schema):
    class Meta:
        fields =('planet_name','planet_type','home_star','mass','radius','distance')


# Instanciate Schemas
user_schema  = UserSchema()             # if a single object
users_schema = UserSchema(many=True)    # if there is multiple object

planet_schema = PlanetSchema()
planets_schema = PlanetSchema(many=True)

if __name__ == '__main__':
    # Runs the application on a local development server.
    # Do not use run() in a production setting. 
    # It is not intended to meet security and performance requirements for a production server. 
    # Instead, see /deploying/index for WSGI server recommendations.
    app.run(host='0.0.0.0', port=5000, debug=True, load_dotenv=True)