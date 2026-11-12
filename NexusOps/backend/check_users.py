
import sqlite3

connection = sqlite3.connect("nexusops.db")
connection.row_factory = sqlite3.Row

users = connection.execute(
    "SELECT id, name, email, role, password_hash FROM users"
).fetchall()

for user in users:
    print("ID :", user["id"])
    print("Nom :", user["name"])
    print("Email :", user["email"])
    print("Rôle :", user["role"])
    print("Mot de passe enregistré :", "Oui" if user["password_hash"] else "Non")
    print("--------------------")

connection.close()
