import os
from typing import Dict

def file_summary(*paths: str) -> Dict:
    summary = {
        "total_files": 0,
        "existing": [],
        "missing": []
    }

    for path in paths:
        if os.path.exists(path):
            summary["total_files"] += 1
            summary["existing"].append({
                "path": path,
                "size": os.path.getsize(path)
            })
        else:
            summary["missing"].append(path)

    return summary

result = file_summary('data/file1.txt', 'data/file2.txt', 'data/file3.txt')

print(result)