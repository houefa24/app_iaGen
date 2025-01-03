import pickle
import pandas as pd
import numpy as np
import os

def inspect_pipeline(pipeline_path):
    """
    Fonction pour inspecter le contenu d'un pipeline scikit-learn et afficher les régions uniques.
    """
    try:
        # Vérifier si le fichier existe
        if not os.path.exists(pipeline_path):
            print(f"Erreur: Le fichier {pipeline_path} n'existe pas.")
            print(f"Répertoire actuel: {os.getcwd()}")
            print("Contenu du répertoire:")
            print(os.listdir('.'))
            return

        # Charger le pipeline
        with open(pipeline_path, 'rb') as file:
            pipeline = pickle.load(file)
        
        print("\n=== DÉTAILS DU PIPELINE ===")
        print(f"Type du pipeline: {type(pipeline)}")
        
        # Inspecter les étapes du pipeline
        if hasattr(pipeline, 'steps'):
            print("\nÉtapes du pipeline:")
            for step_name, step_object in pipeline.steps:
                print(f"\n- Étape '{step_name}':")
                print(f"  Type: {type(step_object)}")
                
                # Afficher les paramètres
                if hasattr(step_object, 'get_params'):
                    params = step_object.get_params()
                    print(f"  Paramètres:")
                    for param_name, param_value in params.items():
                        print(f"    - {param_name}: {param_value}")
        
        # Inspecter les transformers (notamment OneHotEncoder)
        if hasattr(pipeline, 'transformers_'):
            print("\nTransformers:")
            for name, transformer, columns in pipeline.transformers_:
                print(f"\n- Transformer '{name}':")
                print(f"  Colonnes: {columns}")
                print(f"  Type: {type(transformer)}")
                
                # Si transformer est un OneHotEncoder, afficher les catégories pour les régions
                if hasattr(transformer, 'categories_'):
                    if 'region' in columns:
                        print(f"    Catégories (regions): {transformer.categories_}")

                        # Afficher chaque région unique
                        for category in transformer.categories_[0]:
                            print(f"    - {category}")
            
    except Exception as e:
        print(f"Erreur lors de l'inspection du pipeline: {str(e)}")

if __name__ == "__main__":
    # Chemin vers votre pipeline
    # Ajustez ce chemin selon l'emplacement réel de votre fichier
    pipeline_path = "back/models/avocado_pipeline.pkl"  # Mettez ici le bon chemin vers votre fichier
    inspect_pipeline(pipeline_path)
