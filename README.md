# Projet de Prédiction des Ventes et Construction de Pipeline de Données

## Description du Projet

Ce projet vise à prédire les ventes à partir de données historiques en utilisant plusieurs modèles de machine learning et à construire un pipeline de données complet. Le pipeline gère l'extraction, la transformation et le chargement (ETL) des données dans une base de données SQLite. Les performances des modèles sont évaluées pour sélectionner le meilleur modèle pour la prédiction des ventes.

## Structure du Projet

- **Étape 1 : Extraction des Données**
  - Les données sont extraites d'un fichier CSV contenant des informations sur les ventes de produits. Les données incluent des colonnes telles que la date, le produit, la région, les ventes, le prix unitaire, et le stock disponible.

- **Étape 2 : Transformation des Données**
  - Les données sont transformées pour assurer la qualité et la cohérence. Cela inclut la conversion des dates en format `datetime` et la gestion des valeurs manquantes.

- **Étape 3 : Chargement des Données**
  - Les données transformées sont chargées dans une base de données SQLite à l'aide de SQLAlchemy. Cette base de données sert de source pour les analyses et les prédictions.

- **Étape 4 : Modélisation des Données**
  - Plusieurs modèles de machine learning ont été testés, y compris la régression linéaire, Random Forest, XGBoost, KNN, et des modèles simples comme la moyenne mobile, la valeur précédente et le lissage exponentiel simple (SES).
  - Le modèle SES s'est avéré le plus performant, avec un MSE de 581.86 et un R² de 0.2892.

- **Étape 5 : Optimisation et Gestion des Données**
  - Des optimisations supplémentaires ont été effectuées, telles que la création d'index sur les colonnes fréquemment utilisées pour améliorer les performances des requêtes SQL.

- **Étape 6 : Documentation et Présentation des Résultats**
  - Les résultats des analyses ont été documentés et visualisés pour une présentation efficace. Des graphiques comparant les ventes réelles et les prédictions du modèle SES ont été créés.

## Technologies Utilisées

- **Python** : Pour l'extraction, la transformation, et la modélisation des données.
- **Pandas** : Pour la manipulation des données.
- **SQLAlchemy** : Pour l'interaction avec la base de données SQLite.
- **SQLite** : Comme base de données pour stocker les données transformées.
- **Matplotlib** : Pour la visualisation des résultats.
- **Statsmodels** : Pour le lissage exponentiel simple (SES).
- **Git** : Pour le contrôle de version du projet.

## Installation

1. Clonez le dépôt GitHub :

    ```bash
    git clone https://github.com/votre_nom_utilisateur/retail.git
    cd retail
    ```

2. Installez les dépendances Python requises :

    ```bash
    pip install -r requirements.txt
    ```

3. Exécutez le script pour construire le pipeline de données et entraîner les modèles :

    ```bash
    python main.py
    ```

## Fichiers du Projet

- `main.py` : Script principal contenant les étapes de l'ETL, la modélisation des données, et l'optimisation.
- `ventes_produits_synthetiques.csv` : Fichier CSV contenant les données de ventes synthétiques utilisées dans le projet.
- `README.md` : Ce fichier de documentation.

## Résultats

Les résultats montrent que le modèle SES (Simple Exponential Smoothing) est le plus performant pour la prédiction des ventes avec un MSE de 581.86 et un R² de 0.2892. Les autres modèles, bien que testés, n'ont pas fourni des résultats satisfaisants comparés à SES.

## Améliorations Futures

- **Enrichissement des Données** : Ajouter plus de caractéristiques pertinentes pour améliorer les performances des modèles.
- **Exploration de Modèles Avancés** : Tester des modèles de séries temporelles plus avancés comme ARIMA ou Prophet.
- **Déploiement en Production** : Déployer le modèle SES dans un environnement de production en utilisant Docker et des orchestrateurs comme Airflow.

## Contributeurs

- Alexis Zueras

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
