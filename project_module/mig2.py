# Modified function to implement Alternating Approach on the project's total hours
def generate_priority_work_schedule_with_total_hours_alternating(date, projects, task_categories, completed_tasks, output_csv_path,
                                                                max_work_hours=8):
    with open(output_csv_path, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Date', 'Project Name', 'Project ID', 'Task Name', 'Work Hours'])

        remaining_work_hours = max_work_hours  # Remaining work hours for the day

        # Calculate median total hours for determining short-term and long-term projects
        median_total_hours = sorted([project['total_hours'] for project in projects])[len(projects) // 2]

        # Split projects into short-term and long-term
        short_term_projects = [project for project in projects if project['total_hours'] <= median_total_hours]
        long_term_projects = [project for project in projects if project['total_hours'] > median_total_hours]

        # Sort projects within each category by their priority
        short_term_projects.sort(key=lambda x: x['priority'])
        long_term_projects.sort(key=lambda x: x['priority'])

        # Start with the higher priority projects (short-term)
        alternating_flag = True

        # Continue alternating until we run out of work hours or projects
        while (short_term_projects or long_term_projects) and remaining_work_hours > 0:
            current_project_list = short_term_projects if alternating_flag else long_term_projects
            if not current_project_list:
                # If we've run out of projects in the current category, switch to the other
                alternating_flag = not alternating_flag
                continue

            project = current_project_list.pop(0)  # Take the first project from the sorted list
            project_id = project['id']
            project_type = project['type']

            # Get the corresponding tasks for the project
            task_list = task_categories.get(project_type, [])
            for task in task_list:
                if task['task'] in completed_tasks.get(project_id, {}).get('tasks', []):
                    # Skip tasks that have been completed
                    continue
                
                task_hours = random.choice(task['hours'])  # Randomly select hours for the task

                # Check if the task fits into the remaining work hours
                if remaining_work_hours - task_hours >= 0:
                    writer.writerow([date, project['name'], project_id, task['task'], task_hours])
                    remaining_work_hours -= task_hours
                    if project_id not in completed_tasks:
                        completed_tasks[project_id] = {'tasks': [], 'total_hours': 0}
                    completed_tasks[project_id]['tasks'].append(task['task'])
                    completed_tasks[project_id]['total_hours'] += task_hours
                
                # If the current project's total hours are filled or no remaining work hours, move to next project
                if completed_tasks[project_id]['total_hours'] >= project['total_hours'] or remaining_work_hours <= 0:
                    break

            # Toggle the flag for the next iteration to alternate
            alternating_flag = not alternating_flag

        # Warning if work hours remain unassigned
        if remaining_work_hours > 0:
            print(f"****WARNING: 工時未完成，請手動增加工時 ,remaining_work_hours: {remaining_work_hours}****")

# Example usage of the function
# Initialize other necessary variables before calling this function.
# generate_priority_work_schedule_with_total_hours_alternating(sample_date, projects, task_categories, completed_tasks, output_csv_path)

