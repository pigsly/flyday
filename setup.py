from cx_Freeze import setup, Executable

exe1 = Executable(
    script="workDate4.py",
    target_name="migrate.exe"
)

exe2 = Executable(
    script="read_completed_tasks_from_csv3.py",
    target_name="info.exe"
)

exe3 = Executable(
    script="repair.py",
    target_name="repair.exe"
)

exe4 = Executable(
    script="undo.py",
    target_name="undo.exe"
)

setup(
    name = "Daily Task Generator",
    version = "1.0",
    description = "create tasks a Day",    
    executables =[exe1,exe2,exe3,exe4]
)    