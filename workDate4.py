# Import necessary libraries
import csv
import random
from datetime import datetime
import json

with open('projects.json', 'r', encoding='utf-8') as f:
    projects = json.load(f)

with open('project_tasks.json', 'r', encoding='utf-8') as f:
    task_categories = json.load(f)

# Ask user for date
sample_date = input("請輸入日期（MM/dd）：")

# Create a unique CSV file path with current time
current_time = datetime.now().strftime("%Y%m%d%H%M%S")
input_csv_path = 'upload/uploaded_work_schedule.csv'
output_csv_path = f'download/downloaded_work_schedule_{current_time}.csv'
csv_headers = ['DATE(MM/DD)','PROJECTNAME', 'ID', '項目詞彙', '工作時數']

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

            # Clear tasks if total_hours is less than project's total_hours
            if existing_total_hours < project_details['total_hours']:
                existing_tasks.clear()

            for task in sorted(task_list, key=lambda x: x['priority']):
                if task['task'] in existing_tasks:
                    continue

                task_hours = random.choice(task['hours'])

                # Skip tasks that would make remaining_work_hours negative
                if remaining_work_hours - task_hours < 0:
                    continue

                # Skip tasks that exceed the project's total work hours
                if existing_total_hours + task_hours > project_details['total_hours']:
                    continue

                writer.writerow([date, project_details['name'], project_id, task['task'], task_hours])

                # Update remaining work hours for the day
                remaining_work_hours -= task_hours

                if project_id not in completed_tasks:
                    completed_tasks[project_id] = {'tasks': [], 'total_hours': 0}
                completed_tasks[project_id]['tasks'].append(task['task'])
                completed_tasks[project_id]['total_hours'] += task_hours


# Initialize output CSV and Generate work schedule
initialize_csv()
completed_tasks = initialize_completed_tasks(input_csv_path)
generate_priority_work_schedule_with_total_hours(sample_date, projects, task_categories, completed_tasks, output_csv_path)


print("Completed Tasks:")
print(json.dumps(completed_tasks, indent=4, ensure_ascii=False))
