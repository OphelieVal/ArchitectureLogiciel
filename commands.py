from quiz.app import app, db
from quiz.models import *


@app.cli.command("syncdb")
def syncdb():
    db.create_all()
    
@app.cli.command("loaddb")
def loaddb():
    db.drop_all()
    db.create_all()
    quest1 = Questionnaire("Culture G")
    quest2 = Questionnaire("Science")
    quest3 = Questionnaire("Informatique")
    db.session.add_all([quest1, quest2, quest3])
    db.session.commit()

    q1 = Question("Quel est le plus grand océan du monde ?","facile",1)
    q2 = Question("En quelle année a eu lieu le premier pas sur la Lune ?","moyen",1)
    q3 = Question("Qui a peint la Joconde ?","difficile",1)
    db.session.add_all([q1, q2, q3])
    db.session.commit()


    q4 = Question("Quelle est la planète la plus proche du Soleil ?","facile",2)
    q5 = Question("Quel est l'élément chimique le plus abondant dans l’univers ?","moyen",2)
    q6 = Question("Quel organe humain consomme le plus d’oxygène ?","difficile",2)
    db.session.add_all([q4, q5, q6])
    db.session.commit()


    q7 = Question("Dans quel langage est principalement écrit le noyau de Linux ?","facile",3)
    q8 = Question("Quel est le port par défaut du protocole HTTP ?","moyen",3)
    q9 = Question("Que signifie 'DNS' ?","difficile",3)
    db.session.add_all([q7, q8, q9])
    db.session.commit()


