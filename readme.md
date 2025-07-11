# Flyday: Intelligent Efficient Work Hour Planner

[![flyday Release](https://github.com/pigsly/flyday/actions/workflows/release.yml/badge.svg)](https://github.com/pigsly/flyday/actions/workflows/release.yml)
[![CodeQL](https://github.com/pigsly/flyday/actions/workflows/codeql.yml/badge.svg)](https://github.com/pigsly/flyday/actions/workflows/codeql.yml)

<img title="" src="flyday_small.png" alt="Flyday Logo"> [中文版本](/readme.zh.md)

Welcome to Flyday, your Intelligent Efficient Work Hour Planner. Activating Creative Energy-Saving Mode, this tool is designed to reduce daily reporting stress and unleash creativity. Inspired by the well-known database migration tool, Flyway, Flyday is just as adept at managing and orchestrating your daily tasks. With its precision scheduling and efficiency, facilitated through CSV file integration, Flyday ensures that every hour of your workday is optimized for maximum productivity and creative output.

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



Sample output:

<img title="" src="info_sample_en.png" alt="info_sample" width="100%">

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

- priority_method: Provides two priority algorithms. The first is the LongestJobFirst algorithm, where projects with longer work hours have higher priority. The second is the AlternatingApproach algorithm, which alternates between sets of projects with longer and shorter work hours to generate daily tasks. This ensures that shorter tasks are not delayed for too long, making it suitable for months with unforeseen leave or absences. The default setting is AlternatingApproach.

- maxhours: The number of work hours in a day, expressed as a positive number (half-hour increments like `3.5` are supported).

- alternating_flag: True or False, used for recording purposes.

## Usage

After installation, you can use the provided commands to manage your tasks.

### Commands

1. **migrate**  
   Use this command to generate your priority-based work schedule.
   
   ```
   migrate
   ```

2. **info**  
   Provides an overview of the current state of your work schedule.
   
   ```
   info
   ```

3. **repair**  
   In case of any discrepancies in your task schedule, use this command to rearrange the priority of projects.json. The priority will change depending on the  remaining_hours.
   
   ```
   repair
   ```

4. **undo**  
   Reverts the last task migration, in case you wish to backtrack the Schedule.csv and backup a new Schedule_bak.csv
   
   ```
   undo
   ```
   
   Remember, just as migrations in databases, once you've established a routine with Flyday, make it a habit to check your task schedule regularly using the `info` command, and `migrate` your task to your Schedule.csv.

## Contribute

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**. 

## License

Distributed under the Apache License. 

---

Happy task migrating with **Flyday**! If you find this tool useful, please consider giving it a star on GitHub! ✨
