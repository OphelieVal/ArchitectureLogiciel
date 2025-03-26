from flask import abort, app, jsonify, request, url_for, make_response
from quiz.app import app, cors, db
from quiz.models import db, Question, Questionnaire

#Questionnaire

def make_public_questionnaire(questionnaire):
    new_questionnaire = {}
    for field in questionnaire.to_json():
        if field == 'id':
            new_questionnaire['uri'] = url_for('get_questionnaire', id=questionnaire.id, _external=True)
        new_questionnaire[field] = questionnaire.to_json()[field]
    return new_questionnaire

@app.route('/quiz/api/v1.0/questionnaire', methods=['GET'])
def get_les_questionnaires():
    questionnaire = Questionnaire.query.all()
    return jsonify([make_public_questionnaire(q) for q in questionnaire])

@app.route('/quiz/api/v1.0/questionnaire/<int:id>', methods=['GET'])
def get_questionnaire(id):
    questionnaire = Questionnaire.query.get(id)
    if questionnaire is None:
        return None
    return make_public_questionnaire(questionnaire)

@app.route('/quiz/api/v1.0/questionnaire', methods=['POST'])
def create_questionnaire():
    new_questionnaire = Questionnaire(name=request.json['name'])
    db.session.add(new_questionnaire)
    db.session.commit()
    return jsonify({'questionnaire': new_questionnaire.to_json()}), 201

@app.route('/quiz/api/v1.0/questionnaire/<int:id>', methods=['PUT'])
def update_questionnaire(id):
    questionnaire = Questionnaire.query.get(id)
    data = request.get_json()
    questionnaire.name = data.get('name', questionnaire.name)
    db.session.commit()
    return jsonify (questionnaire.to_json())

@app.route('/quiz/api/v1.0/questionnaire/<int:id>', methods=['DELETE'])
def delete_questionnaire(id):
    questionnaire = Questionnaire.query.get(id)
    if questionnaire is None:
        abort(404) 
    Question.query.filter_by(questionnaire_id=id).delete()
    db.session.delete(questionnaire)
    db.session.commit()
    return jsonify('true')

#Question

def make_public_question(question):
    new_question = {}
    for field in question.to_json():
        if field == 'id':
            new_question['uri'] = url_for('get_question', idQuestion=question.idQuestion, _external=True)
        new_question[field] = question.to_json()[field]
    return new_question

@app.route('/quiz/api/v1.0/questionnaire/<int:id>/question', methods=['GET'])
def get_les_questions(id):
    question = Question.query.filter(Question.questionnaire_id == id).all()
    if question is None:
        return None
    return jsonify([make_public_question(q) for q in question])

@app.route('/quiz/api/v1.0/questionnaire/<int:id>/question/<int:idQuestion>', methods=['GET'])
def get_question(id,idQuestion):
    question = Question.query.get(idQuestion)
    if question is None:
        return None
    return make_public_question(question)

@app.route('/quiz/api/v1.0/questionnaire/<int:id>/question', methods=['POST'])
def create_question(id):
    new_question = Question(title=request.json['title'],questionType=request.json['questionType'],questionnaire_id=id)
    db.session.add(new_question)
    db.session.commit()
    return jsonify({'question': new_question.to_json()}), 201

@app.route('/quiz/api/v1.0/questionnaire/<int:id>/question/<int:idQuestion>', methods=['PUT'])
def update_question(id,idQuestion):
    question = Question.query.get(idQuestion)
    data = request.get_json()
    question.title = data.get('title', question.title)
    question.questionType = data.get('questionType', question.questionType)
    db.session.commit()
    return jsonify (question.to_json())

@app.route('/quiz/api/v1.0/questionnaire/<int:id>/question/<int:idQuestion>', methods=['DELETE'])
def delete_question(id,idQuestion):
    question = Question.query.get(idQuestion)
    if question is None:
        abort(404) 
    db.session.delete(question)
    db.session.commit()
    return jsonify('true')

