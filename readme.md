# Flyday: Your Task Migration Assistant

<img title="" src="file:///D:/REPO_PY/flyday/flyday.png" alt="Flyday Logo" width="130">

Welcome to **Flyday**, an intuitive software inspired by the well-known database migration tool, **Flyway**. Just as Flyway manages and orchestrates your database migrations, Flyday ensures that your daily tasks are scheduled with precision and efficiency with CSV file.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
  - [Commands](#commands)
- [Contribute](#contribute)
- [License](#license)

## Introduction

Flyday takes its core philosophy from the concept of migrations in databases. The idea is to streamline the allocation of tasks, ensuring they're effectively prioritized and aptly distributed over time. The primary component of Flyday is the `migrate command`, which is the heart of this task migration system.

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

## Config

1. conf/ projects.json 
   You must give the planed projects this month. flyday will assign the tasks for a day.

2. conf/ project_tasks.json   
   You can defind the type of project, each type owns the specfic tasks. The task can also defind available spending hours.

## Usage

After installation, you can use the provided commands to manage your tasks.

### Commands

1. **migrate**  
   Use this command to generate your priority-based work schedule.

flyday migrate

2. **info**  
   Provides an overview of the current state of your work schedule.

flyday info

3. **repair**  
   In case of any discrepancies in your task schedule, use this command to rearrange the priority of projects.json. The priority will change depending on the  remaining_hours.

flyday repair

4. **clean**  
   Removes all tasks from the current schedule, giving you a clean slate.

flyday clean

5. **undo**  
   Reverts the last task migration, in case you wish to backtrack the Schedule.csv and backup a new Schedule_bak.csv

flyday undo

Remember, just as migrations in databases, once you've established a routine with Flyday, make it a habit to check your task schedule regularly using the `info` command, and `migrate` your task to your Schedule.csv.

## Contribute

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**. 

## License

Distributed under the MIT License. See [LICENSE.md](LICENSE.md) for more information.

---

Happy task migrating with **Flyday**! If you find this tool useful, please consider giving it a star on GitHub! ✨

```

```
