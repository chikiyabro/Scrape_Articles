import  pandas as pd

df = pd.read_csv("Articles.csv",encoding = 'cp1252')
# df = df[df.NewsType != "sports"]
df = df.drop_duplicates(subset=['Heading'], keep='last')
df = df.dropna(subset=['Article'], how='all')

df["Article"] = df["Article"].str.strip('strong>')
df.to_csv("Sports.csv",index=False)
print(df.head())