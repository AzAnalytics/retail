import pandas as pd
from sqlalchemy import create_engine, text

df = pd.read_csv("ventes_produits_synthetiques.csv")
print(df.head())

# Vérifier les valeurs manquantes
missing_values = df.isnull().sum()

# Vérifier les types de données
data_types = df.dtypes

print(missing_values, data_types)
# Conversion de la colonne Date en format datetime
df['Date'] = pd.to_datetime(df['Date'])

# Vérification du changement de type
print(df.dtypes['Date'])

##############################

engine = create_engine("sqlite:///ventes_produits.db")
df.to_sql('ventes',con=engine, if_exists='replace', index=False)

with engine.connect() as conn:
    result = conn.execute(text("SELECT COUNT(*) FROM ventes"))
    row_count = result.fetchone()[0]

print(f"nombre de lignes insérées dans la base de données : {row_count}")

################################

query = """
Select Produit, SUM(Ventes) as Total_Ventes
From ventes
GROUP BY Produit
ORDER BY Total_Ventes DESC
"""

with engine.connect() as conn:
    result = conn.execute(text(query))
    sales_by_product = result.fetchall()

for row in sales_by_product:
    print(row)

"""
le produit numéro 5 est le plus vendu (78268)
"""

query = """
Select Région, SUM(Ventes) as Total_Ventes
From ventes
group by Région
order by Total_Ventes DESC
"""

with engine.connect() as conn:
    result = conn.execute(text(query))
    sales_by_region = result.fetchall()

for row in sales_by_region:
    print(row)

"""
la région numéro 10 a le plus vendu (375146)
"""

#############################

query = """
SELECT strftime('%Y-%m', Date) as Mois, SUM(Ventes) as Total_Ventes
FROM ventes
GROUP BY Mois
ORDER BY Mois
"""

# Exécuter la requête
with engine.connect() as conn:
    result = conn.execute(text(query))
    sales_over_time = result.fetchall()

# Afficher les résultats
for row in sales_over_time:
    print(row)
"""
le mois où il y a le plus de ventes a été réalisé en janvier 2023 (307060)
"""

