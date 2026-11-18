
import sqlite3

from sqlalchemy import select, func, text

from database import engine, Base
import database_models


tables = ["equipments", "users", "incidents"]

sqlite_db = sqlite3.connect("nexusops.db")
sqlite_db.row_factory = sqlite3.Row

Base.metadata.create_all(bind=engine)

try:
    data = {}

    for table_name in tables:
        rows = sqlite_db.execute(
            f"SELECT * FROM {table_name}"
        ).fetchall()

        data[table_name] = [dict(row) for row in rows]

    with engine.begin() as connection:

        for table_name in tables:
            table = Base.metadata.tables[table_name]

            count = connection.execute(
                select(func.count()).select_from(table)
            ).scalar_one()

            if count != 0:
                raise Exception(
                    f"La table {table_name} n'est pas vide. Migration annulée."
                )

        for table_name in tables:
            table = Base.metadata.tables[table_name]

            if data[table_name]:
                connection.execute(
                    table.insert(),
                    data[table_name]
                )

        for table_name in tables:
            connection.execute(
                text(
                    f"""
                    SELECT setval(
                        pg_get_serial_sequence('{table_name}', 'id'),
                        COALESCE(MAX(id), 1),
                        MAX(id) IS NOT NULL
                    )
                    FROM {table_name}
                    """
                )
            )

    print("Migration terminée avec succès !")

    for table_name in tables:
        print(
            table_name,
            ":",
            len(data[table_name]),
            "ligne(s) transférée(s)"
        )

finally:
    sqlite_db.close()
