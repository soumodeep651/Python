import pandas as pd

def parquet_to_csv(parquet_path, csv_path ):
    
    try:
        #Read Parquet file
        df = pd.read_parquet(parquet_path)
        #Convert to CSV
        df.to_csv(csv_path)
        print(f"Convertion has been successful : {csv_path}")

    except Exception as e:
        print(f"An error occured:{e}")

parquet_file = "C:\\Users\Soumodeep\\Desktop\\Data Engineering\\Data Sets\\house-price.parquet"
csv_file = "C:\\Users\\Soumodeep\\Desktop\\Data Engineering\\Data Sets\\house-price.csv"
parquet_to_csv(parquet_file, csv_file)