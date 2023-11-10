import csv
from datetime import datetime
import shutil  # 用於文件操作

def undo(input_csv_path):
    # 創建備份文件
    backup_path = input_csv_path.replace('.csv', '_bak.csv')
    shutil.copy(input_csv_path, backup_path)
    
    # 讀取 CSV 文件
    with open(input_csv_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)  # 讀取標題
        rows = [row for row in reader if any(cell.strip() for cell in row)]  # 跳過空行
    
    # 找到最大日期
    max_date = max(row[0] for row in rows if row)
    
    # 篩選出除了最大日期的所有其他行
    filtered_rows = [row for row in rows if row[0] != max_date]
    
    # 寫回 CSV 文件
    with open(input_csv_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(filtered_rows)

input_csv_path = 'history/Schedule.csv'
undo(input_csv_path)
