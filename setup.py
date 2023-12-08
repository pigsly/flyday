from cx_Freeze import setup, Executable

# Define executables
executables = [
    Executable("migrate.py", target_name="migrate.exe", base="Console", shortcut_name="flyday migrate"),
    Executable("info.py", target_name="info.exe", base="Console", shortcut_name="flyday info"),
    Executable("repair.py", target_name="repair.exe", base="Console", shortcut_name="flyday repair"),
    Executable("undo.py", target_name="undo.exe", base="Console", shortcut_name="flyday undo")
]

# Define package data to include
includefiles = [
    ('conf/projects.json','conf/projects.json'), 
    ('conf/projects_tasks.json','conf/projects_tasks.json'),
    ('conf/config.json','conf/config.json'),
    ('csv/V20231114153243__DAY.csv','csv/V20231114153243__DAY.csv'),
    ('history/Schedule.csv','history/Schedule.csv'),
    ('project_module/ConfigManager.py', 'project_module/ConfigManager.py'),
    ('project_module/ProjectManager.py', 'project_module/ProjectManager.py')
]


setup(
    name="flyday",
    version="1.0",
    description="Create tasks a day",
    executables=executables,
    options={
        'build_exe': {            
            'include_files':includefiles,
            # 'packages': ['ConfigManager'],  # 包含 ConfigManager 模塊
            'build_exe': 'dist/flyday/'  # 指定构建输出的路径
        }
    }
)
