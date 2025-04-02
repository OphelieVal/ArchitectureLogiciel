# ArchitectureLogiciel

## Informations du groupe
AKHTAR Naima
VALIN Ophélie
TD 2A1

## Fonctionnalitées implémentées 

- Récupération serveur : Naima TP précédent
- CRUD sur les questionnaires (add, delete, update)
- CRUD sur les questions (get, add, delete, update)


## Lancer le projet
- Installer un environnement virtuel :  `virtualenv -p python3 venv`    
- Se mettre dans l'environnement virtuel : `source .venv/bin/activate`
- Executer le fichier requirements.txt : `pip install -r requirements.txt`
- Se déplacer dans le répertoire Quiz: `cd quiz/`
- Créer la base de données : `flask syncdb`
- Charger la base de données : `flask loaddb`
- Lancer le serveur : `flask run --debug`
- Se déplacer dans : `cd projettodos/src/`
- Lancer npm : `npm run dev --host` (il faut posséder npm : `npm install`)
- Cliquer sur le lien donné par npm