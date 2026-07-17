from pathlib import Path
import csv

def process_all_csvs(directory: str) -> dict:
    dir_path = Path(directory)
    results = {"processed": [], "failed": []}
    
    for csv_file in dir_path.glob('*.csv'):
        try:
            with open(csv_file, 'r', newline='') as f:
                reader = csv.DictReader(f)
                row_count = sum(1 for _ in reader)
                results["processed"].append({"file": csv_file.name, "rows": row_count})
        except Exception as e:
            results["failed"].append({"file": csv_file.name, "error": str(e)})
    
    return results

fpath= '/home/abhishek/projects/python_prep/data'

res = process_all_csvs(fpath)
print(res)