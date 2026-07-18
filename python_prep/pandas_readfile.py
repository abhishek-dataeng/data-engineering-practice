import pandas as pd

try:
    df = pd.read_csv('/home/abhishek/projects/python_prep/data/sales_data_sample.csv',
                     parse_dates=['ORDERDATE'],dtype = {'SALES': str})
    # print(df.head(5))
    df.info()
except FileNotFoundError as e:
    print(f"Error: {e}. Please check the file path and try again.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")