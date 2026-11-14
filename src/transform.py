import pandas as pd

def transform_data(df):
    df = df.copy()
    colonnes_constantes = [col for col in df.columns if df[col].nunique() == 1]
    df = df.drop(columns=colonnes_constantes)

    df["Attrition"] = df["Attrition"].map({"Yes": 1, "No": 0})
    df["OverTime"] = df["OverTime"].map({"Yes": 1, "No": 0})


    # Catagoriser les tranches d'age
    df['TrancheAge'] = pd.cut(
    df['Age'],
    bins=[18, 30, 40, 50, 65],
    labels=['18-29', '30-39', '40-49', '50+'],
    right=False)

    return df