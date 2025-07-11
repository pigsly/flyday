import csv
import random
from datetime import datetime
import json

input_csv_path = 'history/Schedule.csv'

with open('conf/projects.json', 'r', encoding='utf-8') as f:
    projects = json.load(f)

# Initialize completed_tasks dictionary
completed_tasks = {}

# Read completed tasks from the Schedule.csv file
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
            completed_tasks[project_id].append({'task': task_name, 'hours': float(work_hours)})


# Read completed tasks from the uploaded CSV file
read_completed_tasks_from_csv()

# print(completed_tasks)

# Function to update the priority of projects based on remaining_hours
def update_priority_based_on_remaining_hours(projects, completed_tasks):
    # Calculate remaining_hours for each project
    for project_details in projects:
        project_id = project_details['id']
        remaining_hours = project_details['total_hours']
        for task in completed_tasks.get(project_id, []):
            remaining_hours -= task['hours']
        project_details['remaining_hours'] = remaining_hours

    # Sort the projects by remaining_hours in descending order
    projects.sort(key=lambda x: x['remaining_hours'], reverse=True)

    # Update the priority based on the sorted order
    for i, project_details in enumerate(projects):
        project_details['priority'] = i + 1

    return projects


# Assuming 'projects' and 'completed_tasks' are already defined and populated
# Update the priority and sort the projects
updated_projects = update_priority_based_on_remaining_hours(projects, completed_tasks)

# Save the updated projects back to projects.json
with open('conf/projects.json', 'w', encoding='utf-8') as f:
    json.dump(updated_projects, f, ensure_ascii=False, indent=4)

# Display the updated projects for verification
print(updated_projects)