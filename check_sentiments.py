import pandas as pd
df = pd.read_csv('data/sentimentdataset.csv')
print("Unique Sentiment Values (stripped):")
sentiments = df['Sentiment'].str.strip().unique()
for s in sorted(sentiments):
    count = (df['Sentiment'].str.strip() == s).sum()
    print(f"  '{s}': {count}")
