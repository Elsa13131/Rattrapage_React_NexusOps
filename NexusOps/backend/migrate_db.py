
import sqlite3

connection = sqlite3.connect("nexusops.db")

try:
    columns = {
        row[1]
        for row in connection.execute("PRAGMA table_info(users)")
    }

    if "password_hash" not in columns:
        connection.execute(
            "ALTER TABLE users ADD COLUMN password_hash VARCHAR"
        )
        connection.commit()
        print("Colonne password_hash ajoutée.")
    else:
        print("La colonne password_hash existe déjà.")
finally:
    connection.close()
