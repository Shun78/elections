import pandas as pd

df = pd.read_excel("data/MDB-INSEE-V2.xls", sheet_name=0)
df.to_csv("data/insee_communes.csv", index=False, encoding="utf-8")
print(f"✅ {len(df)} lignes exportées dans data/insee_communes.csv")