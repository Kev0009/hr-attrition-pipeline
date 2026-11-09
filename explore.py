import pandas as pd

df = pd.read_csv("Data/WA_Fn-UseC_-HR-Employee-Attrition.csv")
print(df["Attrition"].value_counts())
print(df.groupby("Department")["Attrition"].apply(lambda s: (s == "Yes").mean().round(3)))
