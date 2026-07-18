import csv


def sum_column_streaming(filepath: str, column: str) -> float:
    total = 0.0
    try:
        with open(filepath, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                total += float(row[column])
        return total
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError as e:
        print(f"Error: {e}")
    except KeyError as e:
        print(f"Error: Column '{column}' not found in the CSV file {e}.")
    except ValueError as e:
        print(f"Error: Could not convert data to float. {e}")


res = sum_column_streaming(
    '/home/abhishek/projects/python_prep/data/sales_data_sample.csv',
    'SALES')
print(res)

#  Sales total: 10032628.85000001
