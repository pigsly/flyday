from cx_Freeze import setup, Executable

# Define executables
executables = [
    Executable("project_module/migrate.py", target_name="migrate.exe"),
    Executable("project_module/info.py", target_name="info.exe"),
    Executable("project_module/repair.py", target_name="repair.exe"),
    Executable("project_module/undo.py", target_name="undo.exe")
]

# Define package data to include
includefiles = [
    ('conf/projects.json','conf/projects.json'), 
    ('conf/projects_tasks.json','conf/projects_tasks.json'),
    ('csv/V20231102144211__DAY.csv','csv/V20231102144211__DAY.csv'),
    ('history/Schedule.csv','history/Schedule.csv')
]


setup(
    name="flyday",
    version="1.0",
    description="Create tasks a day",
    executables=executables,
    options={
        'build_exe': {            
            'include_files':includefiles
        }
    }
)
