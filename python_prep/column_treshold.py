import pandas as pd

# def column_threshold_check(fpath: str, column:str, threshold: float) -> int:
#     rowcount = 0
#     try:
#         with open(fpath,'r',newline='',encoding='utf-8') as f:
#             reader = csv.DictReader(f)
#             for row in reader:
#                 if float(row[column]) > threshold:
#                     rowcount += 1
#         return rowcount
#     except Exception as e:
#         print(f"Error occurred: {e}")


def column_threshold_check(fpath: str, column: str, threshold: float) -> int:
    rowcount = 0
    try:
        df = pd.read_csv(fpath, encoding='utf-8')
        rowcount = df[df[column] > threshold]
        return rowcount.shape[0]
    except Exception as e:
        print(f"Error occurred: {e}")


res = column_threshold_check(
    '/home/abhishek/projects/python_prep/data/sales_data_sample.csv',
    "SALES",
    5000)
print(res)
