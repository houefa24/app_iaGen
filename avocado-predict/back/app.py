from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import pandas as pd
import numpy as np
import logging

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Charger le pipeline
try:
    with open('models/avocado_pipeline.pkl', 'rb') as file:
        preprocessor, model = pickle.load(file)
        logger.info("Pipeline chargé avec succès!")
except Exception as e:
    logger.error(f"Erreur lors du chargement du pipeline: {str(e)}")
    raise

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        logger.info(f"Données reçues: {data}")

        # Créer un DataFrame avec les colonnes attendues
        input_data = pd.DataFrame({
            'Quality1': [data.get('quality1', 0)],
            'Quality2': [data.get('quality2', 0)],
            'Quality3': [data.get('quality3', 0)],
            'Small Bags': [data.get('small_bags', 0)],
            'Large Bags': [data.get('large_bags', 0)],
            'XLarge Bags': [data.get('xlarge_bags', 0)],
            'year': [data.get('year', 2024)],
            'type': [data.get('type', 'conventional')],
            'region': [data.get('region', 'California')]
        })

        # Prétraitement
        X_processed = preprocessor.transform(input_data)
        
        # Prédiction
        prediction = model.predict(X_processed)[0]
        logger.info(f"Prédiction: {prediction}")

        return jsonify({
            'status': 'success',
            'predicted_price': float(prediction)
        })

    except Exception as e:
        logger.error(f"Erreur: {str(e)}")
        return jsonify({
            'status': 'error',
            'error': str(e)
        }), 400

if __name__ == '__main__':
    app.run(debug=True, port=5001)