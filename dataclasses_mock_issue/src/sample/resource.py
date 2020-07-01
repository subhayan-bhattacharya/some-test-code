import flask_restful
import flask
import datetime


class Person:
    def __init__(self, name, year):
        self.name = name
        self.birthyear = year

    def age_of_person(self):
        today = datetime.datetime.now()
        return today.year - self.birthyear


class SampleResource(flask_restful.Resource):
    def __init__(self, person):
        self.person = person

    def get(self):
        age = self.person.age_of_person()
        return flask.jsonify({"name": self.person.name, "age": age})

