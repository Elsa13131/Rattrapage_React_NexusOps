
import sqlite3
from getpass import getpass
from pwdlib import PasswordHash

email = "admin@nexusops.fr"

password = getpass("Nouveau mot de passe : ")
confirmation = getpass("Confirme le mot de passe : ")

if password != confirmation:
    print("Les mots de passe ne correspondent pas.")
    exit()

if len(password) < 8:
    print("Le mot de passe doit contenir au moins 8 caractères.")
    exit()

password_hash = PasswordHash.recommended().hash(password)

connection = sqlite3.connect("nexusops.db")

try:
    cursor = connection.execute(
        "UPDATE users SET password_hash = ? WHERE email = ?",
        (password_hash, email)
    )

    if cursor.rowcount == 0:
        print("Utilisateur introuvable.")
    else:
        connection.commit()
        print("Mot de passe administrateur modifié avec succès.")

finally:
    connection.close()
