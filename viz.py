import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import SimpleExpSmoothing
from main import *
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Convertir les résultats en DataFrame
df_sales_by_product = pd.DataFrame(sales_by_product, columns=['Produit', 'Total_Ventes'])

# Tracer un graphique
plt.figure(figsize=(10, 6))
df_sales_by_product.plot(kind='bar', x='Produit', y='Total_Ventes', legend=False)
plt.title('Ventes Totales par Produit')
plt.ylabel('Total des Ventes')
plt.xlabel('Produit')
plt.show()

# Charger les données depuis SQLite dans un DataFrame
query = "SELECT * FROM ventes"
df = pd.read_sql(query, con=engine)

# Créer des caractéristiques temporelles à partir de la date
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
df['DayOfWeek'] = df['Date'].dt.dayofweek

# Sélectionner les caractéristiques et la cible
features = ['Month', 'Day', 'DayOfWeek', 'Prix unitaire', 'Stock disponible']
X = df[features]
y = df['Ventes']

# Séparer les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# 1. Moyenne Mobile
n = 7  # Fenêtre pour la moyenne mobile
df['Rolling_Mean'] = df['Ventes'].rolling(window=n).mean()

# Décaler d'une période pour éviter la fuite d'information
df['Prediction_Rolling_Mean'] = df['Rolling_Mean'].shift(1)

# Remplir les valeurs manquantes avec la moyenne globale des ventes
df['Prediction_Rolling_Mean'] = df['Prediction_Rolling_Mean'].fillna(df['Ventes'].mean())

# 2. Prédiction Basée sur la Valeur Précédente
df['Prediction_Previous_Value'] = df['Ventes'].shift(1)

# Remplir les valeurs manquantes avec la moyenne globale des ventes
df['Prediction_Previous_Value'] = df['Prediction_Previous_Value'].fillna(df['Ventes'].mean())

# 3. Lissage Exponentiel Simple (SES)
model_ses = SimpleExpSmoothing(df['Ventes']).fit(smoothing_level=0.2, optimized=False)

# Faire des prédictions avec SES et décaler d'une période
df['Prediction_SES'] = model_ses.fittedvalues.shift(-1)

# Remplir les NaN dans la colonne SES par la moyenne des ventes
df['Prediction_SES'] = df['Prediction_SES'].fillna(df['Ventes'].mean())

# Calcul des métriques

# Moyenne Mobile
mse_rolling_mean = mean_squared_error(df['Ventes'], df['Prediction_Rolling_Mean'])
r2_rolling_mean = r2_score(df['Ventes'], df['Prediction_Rolling_Mean'])

# Valeur Précédente
mse_previous_value = mean_squared_error(df['Ventes'], df['Prediction_Previous_Value'])
r2_previous_value = r2_score(df['Ventes'], df['Prediction_Previous_Value'])

# Lissage Exponentiel Simple
mse_ses = mean_squared_error(df['Ventes'], df['Prediction_SES'])
r2_ses = r2_score(df['Ventes'], df['Prediction_SES'])

# Affichage des résultats
print(f"Moyenne Mobile MSE: {mse_rolling_mean}, R²: {r2_rolling_mean}")
print(f"Valeur Précédente MSE: {mse_previous_value}, R²: {r2_previous_value}")
print(f"SES MSE: {mse_ses}, R²: {r2_ses}")

# Vérification des NaN dans les colonnes de prédiction
print(df[['Prediction_Rolling_Mean', 'Prediction_Previous_Value', 'Prediction_SES']].isna().sum())


# Comparaison des ventes réelles avec les prédictions SES
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Ventes'], label='Ventes Réelles', color='blue')
plt.plot(df['Date'], df['Prediction_SES'], label='Prédictions SES', color='red')
plt.title('Comparaison des Ventes Réelles avec les Prédictions SES')
plt.xlabel('Date')
plt.ylabel('Ventes')
plt.legend()
plt.show()
