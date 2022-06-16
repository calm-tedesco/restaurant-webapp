from mongoengine import Document
from mongoengine import DateTimeField, StringField

class Restaurant(Document):
    name = StringField(max_length=60, required=True, unique=True)

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return self.name

class Reservation(Document):
    restaurant = ReferenceField(Restaurant, required=True)
    date = DateTimeField()
    description = StringField(max_length=240)
    customer = StringField(max_length=60)
    phone_contact = StringField(max_length=20)
