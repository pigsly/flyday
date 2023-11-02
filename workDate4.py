# Import necessary libraries
import csv
import random
import datetime
import json
import os

with open('conf/projects.json', 'r', encoding='utf-8') as f:
    projects = json.load(f)

with open('conf/project_tasks.json', 'r', encoding='utf-8') as f:
    task_categories = json.load(f)

# Ask user for date
# 獲取當前日期
current_date = datetime.datetime.today()
formatted_date = current_date.strftime('%m/%d')

# 讓使用者輸入日期，預設為今天日期
sample_date = input(f"請輸入日期（MM/dd）（預設：{formatted_date}）：") or formatted_date

print(f"您選擇的日期是：{sample_date}")


# Create a unique CSV file path with current time
current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
input_csv_path = 'history/uploaded_work_schedule.csv'
output_csv_path = f'csv/downloaded_work_schedule_{current_time}.csv'
csv_headers = ['DATE(MM/DD)','PROJECTNAME', 'ID', '項目詞彙', '工作時數']


'''
date: 輸入的日期。
projects: 從 projects.json 讀取的項目列表。
task_categories: 從 project_tasks.json 讀取的任務類別。
completed_tasks: 已完成的任務和對應的總工時。
output_csv_path: 輸出 CSV 文件的路徑。
max_work_hours: 一天中可分配的最大工作時數。
'''
def initialize_csv():
    with open(output_csv_path, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(csv_headers)

def initialize_completed_tasks(input_csv_path):
    completed_tasks = {}
    try:
        with open(input_csv_path, mode='r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # Skip headers

            for row in reader:
                if len(row) == 0:  # Skip empty rows
                    continue
                date, project_name, project_id, task_name, work_hours = row
                if project_id not in completed_tasks:
                    completed_tasks[project_id] = {'tasks': [], 'total_hours': 0}
                completed_tasks[project_id]['tasks'].append(task_name)
                completed_tasks[project_id]['total_hours'] += int(work_hours)
    except FileNotFoundError:
        print("Warning: uploaded_work_schedule.csv not found. Starting with an empty completed_tasks dictionary.")
    return completed_tasks


def generate_priority_work_schedule_with_total_hours(date, projects, task_categories, completed_tasks, output_csv_path,
                                                     max_work_hours=8):
    with open(output_csv_path, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Date', 'Project Name', 'Project ID', 'Task Name', 'Work Hours'])

        remaining_work_hours = max_work_hours  # Remaining work hours for the day

        for project_details in sorted(projects, key=lambda x: x['priority']):
            project_id = project_details['id']
            project_type = project_details['type']

            if project_type not in task_categories:
                continue

            task_list = task_categories[project_type]
            existing_tasks = completed_tasks.get(project_id, {}).get('tasks', [])
            existing_total_hours = completed_tasks.get(project_id, {}).get('total_hours', 0)
            
            # 如果任務都已經做過，則任務全部重新開放。
            available_tasks = [task for task in task_list if task['task'] not in existing_tasks]
            if not available_tasks:
                available_tasks = task_list

            for task in sorted(available_tasks, key=lambda x: x['priority']):
                
                task_hours = random.choice(task['hours'])

                # Skip tasks that would make remaining_work_hours negative
                if remaining_work_hours - task_hours < 0:
                    continue

                # Skip tasks that exceed the project's total work hours
                if existing_total_hours + task_hours > project_details['total_hours']:
                    continue

                writer.writerow([date, project_details['name'], project_id, task['task'], task_hours])
                # print(f"{project_details['name']}, {project_id}, {task['task']}, {task_hours}")
                # Update remaining work hours for the day
                remaining_work_hours -= task_hours
                # 更新此專案當前完成工時（剛剛產出的工時）
                existing_total_hours += task_hours
                # print(f"remaining_work_hours: {remaining_work_hours}, existing_total_hours: {existing_total_hours} ")
                
                if project_id not in completed_tasks:
                    completed_tasks[project_id] = {'tasks': [], 'total_hours': 0}
                completed_tasks[project_id]['tasks'].append(task['task'])
                completed_tasks[project_id]['total_hours'] += task_hours
    if(remaining_work_hours > 0 and max_work_hours > remaining_work_hours):
        print(f"****WARRNING: 工時未完成，請手動增加工時 ,remaining_work_hours: {remaining_work_hours}****")            




# Initialize output CSV and Generate work schedule
initialize_csv()
completed_tasks = initialize_completed_tasks(input_csv_path)
generate_priority_work_schedule_with_total_hours(sample_date, projects, task_categories, completed_tasks, output_csv_path)


# print("Completed Tasks:")
# print(json.dumps(completed_tasks, indent=4, ensure_ascii=False))



def append_csv_content(input_csv_path, output_csv_directory):
    # 獲取目錄中的所有文件並按最後修改時間排序
    list_of_files = os.listdir(output_csv_directory)
    csv_files = [f for f in list_of_files if f.startswith('downloaded_work_schedule_') and f.endswith('.csv')]
    csv_files.sort(key=lambda x: os.path.getmtime(os.path.join(output_csv_directory, x)), reverse=True)
    
    # 選擇最新的csv檔
    latest_csv_file = csv_files[0]
    print(f"latest_csv_file:{latest_csv_file}")
    output_csv_path = os.path.join(output_csv_directory, latest_csv_file)

    # 讀取該csv檔（跳過第一行）並附加到input_csv_path
    with open(input_csv_path, 'a', newline='', encoding='utf-8') as input_file:
        writer = csv.writer(input_file)
         # 寫入一個空行
        writer.writerow([])
        with open(output_csv_path, 'r', newline='', encoding='utf-8') as output_file:
            reader = csv.reader(output_file)
            next(reader)  # 跳過第一行
            for row in reader:
                writer.writerow(row)

# 使用範例
append_csv_content(input_csv_path, 'csv/')
