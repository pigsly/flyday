import csv
import random
from datetime import datetime
import json

input_csv_path = 'history/Schedule.csv'

with open('conf/projects.json', 'r', encoding='utf-8') as f:
    projects = json.load(f)

# Initialize completed_tasks dictionary
completed_tasks = {}

# Read completed tasks from the uploaded_work_schedule.csv file
def read_completed_tasks_from_csv():
    with open(input_csv_path, mode='r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header row
        for row in reader:
            if len(row) == 0:  # Skip empty rows
                    continue
            date,  projectname, project_id, task_name, work_hours = row
            if project_id not in completed_tasks:
                completed_tasks[project_id] = []
            completed_tasks[project_id].append({'task': task_name, 'hours': int(work_hours)})


# Read completed tasks from the uploaded CSV file
read_completed_tasks_from_csv()

# print(completed_tasks)



# Display the updated projects for verification
# print(updated_projects)


# Your function to print remaining work hours
def print_remaining_hours():
    for project_details in projects:
        project_id = project_details['id']
        remaining_hours = project_details['total_hours']
        for task in completed_tasks.get(project_id, []):
            remaining_hours -= task['hours']
        print(f"{project_id} ({project_details['name']})({project_details['priority']}) - remaining hours：{remaining_hours} H")


def total_remaining_hours():
    total_hours = 0
    for project_details in projects:
        project_id = project_details['id']
        remaining_hours = project_details['total_hours']
        for task in completed_tasks.get(project_id, []):
            remaining_hours -= task['hours']
        total_hours += remaining_hours
    return total_hours

def total_projects_hours():
    total_hours = 0
    for project_details in projects:
        project_id = project_details['id']
        project_hours = project_details['total_hours']
        total_hours += project_hours
    return total_hours

# Print remaining work hours for each project
print_remaining_hours()
tph = total_projects_hours()
trh = total_remaining_hours()
tuh = tph - trh
print(f"**Total project hours: {tph} H, Total remaining project hours: {trh} H, Total used hours: {tuh} H**")


# Here follows the rest of your code
# ... (your projects, project_tasks, initialize_csv, and generate_priority_work_schedule functions)
