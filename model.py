from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()

class User(db.Model):
    "User of Then and Now."

    __tablename__ = "users"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(200), nullable=False)
    first_name = db.Column(db.String(32), nullable=False)
    middle_name = db.Column(db.String(32), nullable=True)
    last_name = db.Column(db.String(32), nullable=False)
    facebook_id = db.Column(db.String(50), nullable=True)
    profile_picture = db.Column(db.String(200), default="https://s3-us-west-1.amazonaws.com/wanderlist-images/Wanderlust+Logo.png")
    school_class_id = db.Column(db.Integer, db.ForeignKey('school_classes.id'), nullable=True)
    birthday = db.Column(db.DateTime, nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=True)
    active = db.Column(db.Boolean, default=False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User id: {}, name: {} {}>".format(self.id, self.first_name, self.last_name)

    school_class = db.relationship('SchoolClass')

    location = db.relationship('Location')



class SchoolClass(db.Model):
    """Information about a school class. Ex: Class of 2010."""

    __tablename__ = "school_classes"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    # valedictorian = 
    # saluatorian = 

    users = db.relationship('User')


    # school_class = db.relationship("SchoolClass", 
    #                                     backref=db.backref("users",
    #                                             order_by=school_class_id))



class Location(db.Model):
    """Information about a location."""

    __tablename__ = 'locations'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    address = db.Column(db.String(200), nullable=False)
    postal_code = db.Column(db.String(5), nullable=False)
    country = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Location id: {}, name: {}".format(self.id, self.name)



