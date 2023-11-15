# Flyday: Your Task Migration Assistant

<img title="" src="flyday.png" alt="Flyday Logo" width="130">

Welcome to **Flyday**, an intuitive software inspired by the well-known database migration tool, **Flyway**. Just as Flyway manages and orchestrates your database migrations, Flyday ensures that your daily tasks are scheduled with precision and efficiency with CSV file.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
  - [First Step, arrange your works this month.]
  - [Second Step, Review Config]
  - [Commands](#commands)
- [Contribute](#contribute)
- [License](#license)

## Introduction

Flyday uses the concept of database migrations to streamline task allocation. It prioritizes tasks and distributes them over time, allowing you to track your work hours and modify the schedule if necessary.

Key Features:

1. Uses CSV files for easy viewing and editing in office software.
2. Flyway-like command management for ease of use.
3. Extensible priority algorithms.

Flyday 從資料庫遷移的概念中汲取其核心理念。其目的是簡化任務分配，確保任務得到有效的優先排序並適當地分佈在時間上。使用 Flyday 可以指導您撰寫每日的工作記錄，並清晰地了解該月的工時結構。如果指導生成的每日工作記錄不適合，您也可以方便地手動修改 history/Schedule.csv。

其設計的核心要點包括：

1. 使用 CSV 檔案作為存儲容器，方便用 Office 軟件查看工作結果。
2. 使用類似 Flyway 的管理指令，只要您熟悉 Flyway 就能快速上手。
3. 優先權算法可以擴充。

## Installation

1. Clone the repository:

2. Create virtualenv   
   
   ```
   virtualenv venv
   .\venv\Scripts\activate
   ```

3. Install necessary dependencies:
   
   ```
   pip install -r requirements.txt
   ```

4. Run the setup script (if any):
   
   ```
   python setup.py install
   ```

## First Step, arrange your works this month.

1. conf/ projects.json 
   You must give the planed projects this month. flyday will assign the tasks for a day.

2. conf/ project_tasks.json   
   You can defind the type of project, each type owns the specfic tasks. The task can also defind available spending hours.

## Second Step, Review Config.
In conf/config.json:

- priority_method: Provides two priority algorithms. The first is the LongestJobFirst algorithm, where projects with longer work hours have higher priority. The second is the AlternatingApproach algorithm, which alternates between sets of projects with longer and shorter work hours to generate daily tasks. This ensures that longer tasks are not delayed for too long, making it suitable for months with unforeseen leave or absences. The default setting is AlternatingApproach.

- maxhours: The number of work hours in a day, expressed as a positive integer.

- alternating_flag: True or False, used for recording purposes.

## Usage

After installation, you can use the provided commands to manage your tasks.

### Commands

1. **migrate**  
   Use this command to generate your priority-based work schedule.
```
flyday migrate
```
2. **info**  
   Provides an overview of the current state of your work schedule.
```
flyday info
```
3. **repair**  
   In case of any discrepancies in your task schedule, use this command to rearrange the priority of projects.json. The priority will change depending on the  remaining_hours.
```
flyday repair
```
4. **undo**  
   Reverts the last task migration, in case you wish to backtrack the Schedule.csv and backup a new Schedule_bak.csv
```
flyday undo
```
Remember, just as migrations in databases, once you've established a routine with Flyday, make it a habit to check your task schedule regularly using the `info` command, and `migrate` your task to your Schedule.csv.

## Contribute

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**. 

## License

Distributed under the Apache License. 

---

Happy task migrating with **Flyday**! If you find this tool useful, please consider giving it a star on GitHub! ✨


