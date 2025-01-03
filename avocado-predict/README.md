# Prédicteur de Prix d'Avocats 🥑

Cette application fullstack permet de prédire le prix moyen des avocats en utilisant une pipeline. Elle utilise Flask pour le backend et Streamlit pour le frontend.

## Structure du Projet

## prompt : Génère moi le code pour pour une application fonctionnelle et optimisée fullstack avec flask pour la partie backend et Streamlit pour la partie frontend.
```
avocado-predict/
├── backend/
│   └── models
│       └── avocado_pipeline.pkl
|  └── app.py
|   └── requirements.txt
├── frontend/
|   └── streamlit_app.py
|   └── requirements.txt
└── README.md
└── test_pipeline.py
```


1. Créer un environnement virtuel :
```bash
python -m venv .venv
source .venv/bin/activate  # Sur Windows : .venv\Scripts\activate
```

2. Installer les dépendances :
mettre les dépendances dans le fichier requirement.txt pour le front et le back. 
```bash
installer dépendances pour le back 
cd back 
pip install -r requirements.txt

installer dépendances pour le front 
cd front
pip install -r requirements.txt
```

3. Créer un fichier inspect.pipeline.py  à la racine du projet pour inspecter la pipeline 
## prompt : "Pouvez-vous me fournir un script Python qui inspecte en détail le contenu d'un pipeline
## scikit-learn sauvegardé dans un fichier pickle ? Le script devrait :
## Charger le pipeline depuis un fichier .pkl
## Afficher la structure de la pipeline 
## Afficher les données de la pipeline
## ou autres informations pouvant être utiles pour créer une application fullsatcak à partir de ce modèle d'entraînement.

```bash
python inspect_pipeline.py

```

4. Créer une application fullstack 
## prompt : Maintenant que tu as inspecté ma pipeline , génères moi un code pour une application fullstack optimisée et fonctionelle.
## Maintenant organise regroupe moi les niveaux de qaulité ensembles comme tu la fait avec les types de sacs. 


## Utilisation

1. Lancer le backend (dans un terminal) :
```bash
cd back
python3 app.py
```

2. Lancer le frontend (dans un autre terminal) :
```bash
cd front
streamlit run streamlit_app.py
```

3. Ouvrir votre navigateur à l'adresse indiquée : http://localhost:8501

## Fonctionnalités

- Prédiction du prix des avocats basée sur différentes caractéristiques. 
- Classement des caractéritiques de la pipe line en 2 c&tégories : numériques et catégorielles 
- API REST pour les prédictions
- Gestion des erreurs

## Technologies Utilisées

- Backend : Flask, scikit-learn, XGBoost
- Frontend : Streamlit
- Modèle d'entraînment : Pipeline scikit-learn, XGBoost

## Auteur

Laura Baratier et Romance 

## Licence

Ce projet est sous licence MIT.