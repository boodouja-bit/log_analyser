
import sqlite3

from ingestion import raw
from process.extract_transforme import extract_from_row


# 1. Lire toutes les lignes
rows = raw.toRows('./data')

print("Nombre total de lignes :", len(rows))


# 2. Créer la base de données
connection = sqlite3.connect('logs.db')

cursor = connection.cursor()


# 3. Créer la table
cursor.execute("""
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    month TEXT,
    day INTEGER,
    time TEXT,
    service TEXT,
    message TEXT
)
""")


# 4. Extraire et enregistrer toutes les lignes
extracted = 0
not_extracted = 0

for row in rows:

    data = extract_from_row(row)

    if data is not None:

        cursor.execute("""
        INSERT INTO logs (month, day, time, service, message)
        VALUES (?, ?, ?, ?, ?)
        """, (
            data["month"],
            data["day"],
            data["time"],
            data["service"],
            data["message"]
        ))

        extracted += 1

    else:
        not_extracted += 1


# 5. Enregistrer les modifications
connection.commit()


# 6. Afficher les statistiques
print("\n===== RESULTAT =====")
print("Lignes lues :", len(rows))
print("Lignes extraites :", extracted)
print("Lignes non extraites :", not_extracted)


# 7. Vérifier la base
cursor.execute("SELECT COUNT(*) FROM logs")

print("Nombre d'enregistrements dans la base :",
      cursor.fetchone()[0])


connection.close()
