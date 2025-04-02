# ArchitectureLogiciel

## Sujet    
Construire une application Vue pour des questionnaires. Cette application doit se connecter à un serveur REST. Il doit être possible de récupérer, modifier, créer et supprimer des questionnaires et des questions.    


## Commandes Utiles
`npm run dev --host`


### Si l'environnement virtuel n'est pas présent    
- Installer un environnement virtuel :  `virtualenv -p python3 venv`    

### Par la suite
- Se mettre dans l'environnement virtuel : `source .venv/bin/activate`
- Executer le fichier requirements.txt : `pip install -r requirements.txt`
- Se déplacer dans le répertoire Quiz: `cd quiz/`
- Créer la base de données : `flask syncdb`
- Charger la base de données : `flask loaddb`
- Lancer le serveur : `flask run --debug`
- Ouvrir le fichier quiz.html ()