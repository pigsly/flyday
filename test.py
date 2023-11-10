import json

# 這是你的 JSON 數據
data = {
  "專案類": [
    {"task": "專案建置設定", "hours": [1, 1], "priority": 1},
    {"task": "GIT配置", "hours": [1, 1], "priority": 2},
    {"task": "資料庫調整", "hours": [1, 4], "priority": 3},
    {"task": "功能客製", "hours": [1, 16], "priority": 4},
    {"task": "測試工作", "hours": [1, 4], "priority": 5},
    {"task": "客戶測試回饋與討論", "hours": [1, 3], "priority": 6},
    {"task": "連線配置與部署工作", "hours": [1, 1], "priority": 7}
  ],
  "遠時維運類": [
    {"task": "客戶溝通說明", "hours": [1, 2], "priority": 1}
  ],
  "維運類": [
    {"task": "環境檢查", "hours": [1, 1], "priority": 1},
    {"task": "監測訊息調查", "hours": [1, 1], "priority": 2},
    {"task": "可疑資料比對", "hours": [1, 1], "priority": 3},
    {"task": "客戶溝通說明", "hours": [1, 8], "priority": 4}
  ]
}

# 尋找所有 "hours" 欄位有可能等於 3 的任務
tasks_with_hours_3 = []

for category, tasks in data.items():
    for task in tasks:
        if 3 >= task['hours'][0] and 3 <= task['hours'][1]:
            tasks_with_hours_3.append({
                'category': category,
                'task_name': task['task'],
                'hours_range': task['hours']
            })

# 輸出結果
print("Tasks where 'hours' could be 3 are:")
for task in tasks_with_hours_3:
    print(f"Category: {task['category']}, Task: {task['task_name']}, Hours Range: {task['hours_range']}")
