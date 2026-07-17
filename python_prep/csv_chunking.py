import pandas as pd

def sum_column_chunk(filepath: str, column:str, chunk_size= 10000) -> float:
    total = 0.0
    try:
        for chunk in pd.read_csv(filepath,chunksize=chunk_size):
            total += chunk[column].sum()
        return total
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError as e:
        print(f"Error: {e}")
    except KeyError as e:
        print(f"Error: Column '{column}' not found in the CSV file.")   

res = sum_column_chunk('/home/abhishek/projects/python_prep/data/sales_data_sample.csv','SALES')
print(res)