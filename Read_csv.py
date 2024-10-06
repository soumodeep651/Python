import pandas as pd
try:
    df = pd.read_csv("C:\\Users\\Soumodeep\\Desktop\\Data Engineering\\Data Sets\\house-price.csv")
    df= df.drop('Index', axis =1)
    #print(df.head(5))
    result = df[(df["price"] >= 11410000) & (df["furnishingstatus"] == 'furnished') ]
    print(result)

except Exception as e:
    print(f"An error occured {e}")