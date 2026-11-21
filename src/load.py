import sqlite3
from pathlib import Path

def load(df, db_path="data/processed/hr.db", table="employees"):
    # 1. Créer le dossier data/processed s'il n'existe pas
    Path(db_path).parent.mkdir(parents=True, exist_ok=True)

    # 2. Ouvrir la base et y écrire le DataFrame
    with sqlite3.connect(db_path) as conn:
        df.to_sql(table, conn, if_exists="replace", index=False)

    print(f"{len(df)} lignes chargées dans la table '{table}' ({db_path})")