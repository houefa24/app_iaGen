import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Prédiction Prix Avocats", page_icon="🥑", layout="wide")

st.title('Avocado Predict 🥑 ')
st.markdown("<h4 style='color: gray;'>Modifiez les caractéristiques ci-dessous pour prédire le prix moyen des avocats aux États-Unis</h4>", unsafe_allow_html=True)

def create_input_features():
    st.markdown("## 📊 CARACTÉRISTIQUES NUMÉRIQUES")
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("<div style='font-size: 24px; font-weight: bold;'>Niveaux de qualité</div>", unsafe_allow_html=True)
        quality1 = st.number_input('Quality1', min_value=0.00, value=1.0, help="Niveau de qualité 1", key="qual1")
        quality2 = st.number_input('Quality2', min_value=0.00, value=1.0, help="Niveau de qualité 2", key="qual2")
        quality3 = st.number_input('Quality3', min_value=0.00, value=1.0, help="Niveau de qualité 3", key="qual3")

    with col2:
        st.markdown("<div style='font-size: 24px; font-weight: bold;'>Types de Sacs</div>", unsafe_allow_html=True)
        small_bags = st.number_input('Small Bags', min_value=0.00, value=1.0, help="Petits sacs", key="small")
        large_bags = st.number_input('Large Bags', min_value=0.00, value=1.0, help="Grands sacs", key="large")
        xlarge_bags = st.number_input('XLarge Bags', min_value=0.00, value=1.0, help="Très grands sacs", key="xlarge")

    with col3:
        st.markdown("<div style='font-size: 24px; font-weight: bold;'>Année</div>", unsafe_allow_html=True)
        year = st.number_input('Année', min_value=2000, max_value=2024, value=2024, key="year")
    
    st.markdown("---")
    st.markdown("## 📋 CARACTÉRISTIQUES CATÉGORIELLES")
    col4, col5 = st.columns(2)
    
    with col4:
        st.markdown("<div style='font-size: 24px; </div>", unsafe_allow_html=True)
        type_avocat = st.selectbox('Type d\'avocat', ['conventional', 'organic'], key="type")

    with col5:
        st.markdown("<div style='font-size: 24px;</div>", unsafe_allow_html=True)
    
    # Liste des régions
    regions = [
        'Albany', 'Atlanta', 'BaltimoreWashington', 'Boise', 'Boston', 'BuffaloRochester',
        'California', 'Charlotte', 'Chicago', 'CincinnatiDayton', 'Columbus', 'DallasFtWorth',
        'Denver', 'Detroit', 'GrandRapids', 'GreatLakes', 'HarrisburgScranton', 'HartfordSpringfield',
        'Houston', 'Indianapolis', 'Jacksonville', 'LasVegas', 'LosAngeles', 'Louisville',
        'MiamiFtLauderdale', 'Midsouth', 'Nashville', 'NewOrleansMobile', 'NewYork', 'Northeast',
        'NorthernNewEngland', 'Orlando', 'Philadelphia', 'PhoenixTucson', 'Pittsburgh', 'Plains',
        'Portland', 'RaleighGreensboro', 'RichmondNorfolk', 'Roanoke', 'Sacramento', 'SanDiego',
        'SanFrancisco', 'Seattle', 'SouthCarolina', 'SouthCentral', 'Southeast', 'Spokane',
        'StLouis', 'Syracuse', 'Tampa', 'TotalUS', 'West', 'WestTexNewMexico'
    ]
    
    # Affichage du selectbox avec toutes les régions
    region = st.selectbox('Région de vente', regions, key="region")

# Affichage de la région sélectionnée
    st.write(f'Région sélectionnée: {region}')


    return {
        'quality1': quality1,
        'quality2': quality2,
        'quality3': quality3,
        'small_bags': small_bags,
        'large_bags': large_bags,
        'xlarge_bags': xlarge_bags,
        'year': year,
        'type': type_avocat,
        'region': region
    }

def predict_price(features):
    try:
        response = requests.post(
            'http://localhost:5001/predict',
            json=features,
            headers={'Content-Type': 'application/json'}
        )
        
        if response.status_code == 200:
            result = response.json()
            st.success(f"Prix prédit : ${result['predicted_price']:.2f}")
        else:
            st.error(f"Erreur: {response.text}")
            
    except requests.exceptions.ConnectionError:
        st.error("Impossible de se connecter au serveur. Vérifiez que le backend est en cours d'exécution.")
    except Exception as e:
        st.error(f"Erreur: {str(e)}")

def main():
    features = create_input_features()
    
    if st.button('Prédire le Prix', type='primary'):
        st.write("Données utilisées:", features)
        predict_price(features)

    with st.expander("À propos du modèle"):
        st.write("""
        Ce modèle utilise XGBoost pour prédire les prix des avocats en se basant sur :
        - Les niveaux de qualité
        - Les types d'emballage
        - L'année
        - La région de vente
        - Le type d'avocat (conventionnel ou organique)
        """)

if __name__ == "__main__":
    main()