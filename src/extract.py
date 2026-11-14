from pathlib import Path
import pandas as pd

COLONNES_REQUISES = {"EmployeeNumber", "Attrition", "Department", "MonthlyIncome","OverTime"}

def extract(path):
    # 1. Vérifie si le fichier existe
    if not Path(path).exists():
        raise FileNotFoundError(f"Le fichier {path} n'existe pas.")

    # 2. Lit le fichier CSV
    df = pd.read_csv(path)

    # 3. Vérifie si les colonnes requises sont présentes
    manquantes = COLONNES_REQUISES - set(df.columns)
    if manquantes:
        raise ValueError(f"Colonnes manquantes : {manquantes}")


    #4. Afficher la taille de la DataFrame (lignes et colonnes)
    print(f"Taille du DataFrame : {df.shape[0]} lignes, {df.shape[1]} colonnes")

    return df