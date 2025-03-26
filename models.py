from flask_sqlalchemy import SQLAlchemy
from quiz.app import app, db

class Questionnaire(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Questionnaire(%d)%s>"%(self.id, self.name)

    def to_json(self):
        json = {
          'id' : self.id,
          'name' : self.name
        }
        return json

    def get_id_questionnaire(self):
        return self.id

    def get_name_questionnaire(self):
        return self.name

    def set_name_questionnaire(self, name):
        self.name = name


class Question(db.Model):
    idQuestion = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(120))
    questionType = db.Column(db.String(120))
    questionnaire_id = db.Column(db.Integer, db.ForeignKey('questionnaire.id'))
    questionnaire = db.relationship("Questionnaire", backref = db.backref("questions", lazy = "dynamic"))

    def __init__(self, title, questionType, questionnaire_id):
        self.title = title
        self.questionType = questionType
        self.questionnaire_id = questionnaire_id

    def to_json(self):
        json = {
          'idQuestion' : self.idQuestion,
          'title' : self.title,
          'questionType' : self.questionType,
          'questionnaire_id' : self.questionnaire_id,
        }
        return json

    def get_id_question(self):
        return self.idQuestion

    def get_title_question(self):
        return self.title

    def set_title_question(self, title):
        self.title = title

    def get_type_question(self):
        return self.questionType

    def set_type_question(self, type):
        self.questionType = type

    def delete_question(self):
        db.session.delete(self)
        db.session.commit()

    def add_question(self):
        db.session.add(self)
        db.session.commit()

    def change_question(self, title, questionType, questionnaire_id):
        res = Question.query.filter_by(idQuestion=self.idQuestion).first()
        res.title = title
        res.questionType = questionType
        res.questionnaire_id = questionnaire_id
        db.session.commit()

# Ajouter de l'héritage sur les questions, questions à choix multiple (OpenQuestions) champ qui coincident, et les questions simples (SimpleQuestion)