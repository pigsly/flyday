import csv
import json

class ProjectManager:
    def __init__(self, input_csv_path, conf_projects_path):
        self.input_csv_path = input_csv_path
        self.conf_projects_path = conf_projects_path
        self.projects = []
        self.completed_tasks = {}
        self.readProjects()
        self.refresh_completed_tasks() 


    def readProjects(self):
        with open(self.conf_projects_path, 'r', encoding='utf-8') as f:
            self.projects = json.load(f)

    # useful
    def refresh_completed_tasks(self):        
        with open(self.input_csv_path, mode='r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # Skip headers
            for row in reader:
                if len(row) == 0:  # Skip empty rows
                    continue
                date, project_name, project_id, task_name, work_hours = row
                if project_id not in self.completed_tasks:
                    self.completed_tasks[project_id] = {'tasks': [], 'total_hours': 0}
                self.completed_tasks[project_id]['tasks'].append(task_name)
                self.completed_tasks[project_id]['total_hours'] += int(work_hours)
    
    # 這是演算法處理期間可運用的method     
    def update_priority_based_on_remaining_hours(self):
        for project_details in self.projects:
            project_id = project_details['id']
            remaining_hours = project_details['total_hours']
            # 检索项目的已完成任务和总工时
            project_tasks = self.completed_tasks.get(project_id, {'tasks': [], 'total_hours': 0})
            task_hours = project_tasks['total_hours']
            remaining_hours -= task_hours
            project_details['remaining_hours'] = remaining_hours

        # Sort the projects by remaining_hours in descending order
        self.projects.sort(key=lambda x: x['remaining_hours'], reverse=True)

        # Update the priority based on the sorted order
        for i, project_details in enumerate(self.projects):
            project_details['priority'] = i + 1

    # useful 
    # reset means read the data from input_csv_path
    def reset_and_reload_completed_tasks(self):
            # 清空 completed_tasks 字典
            self.completed_tasks.clear()
            # 重新从 CSV 文件中读取数据
            self.refresh_completed_tasks()

    # 這是演算法處理期間可運用的method   
    def get_projects_with_bigger_remaining_hours(self, hours):
        # 使用列表推导式过滤掉 remaining_hours 为 0 的项目
        return [project for project in self.projects if project['remaining_hours'] > hours]


    @classmethod
    def get_instance(cls, input_csv_path, conf_projects_path):
        return cls(input_csv_path, conf_projects_path)

# 使用示例
# manager = ProjectManager.get_instance('path_to_your_csv_file.csv')
# manager.read_completed_tasks_from_csv('path_to_your_csv_file.csv')
# manager.update_priority_based_on_remaining_hours()
# print(manager.projects)
