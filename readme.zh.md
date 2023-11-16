# Flyday: 任務遷移助手 
[English Version](README.md)

<img title="" src="flyday.png" alt="Flyday Logo" width="130">

歡迎來到 **Flyday**，啟動創意節能模式：減壓報每日工時，釋放創造力！，一款靈感來自著名的數據庫遷移工具 **Flyway** 的直觀軟件。就像 Flyway 管理和協調您的數據庫遷移一樣，Flyday 確保您的日常任務能夠通過 CSV 文件精確且高效地進行每日工作排程。

## 目錄

- [介紹](#介紹)
- [安裝](#安裝)
- [使用方法](#使用方法)
  - [第一步，安排本月工作。](#第一步)
  - [第二步，審查配置](#第二步)
  - [指令](#指令)
- [貢獻](#貢獻)
- [許可證](#許可證)

## 介紹

Flyday 從數據庫遷移的概念中汲取靈感，用於精簡任務分配。它優先排序任務並在時間上分佈，讓您跟蹤工作時數並在必要時調整日程。

核心功能：

1. 使用 CSV 文件，便於在辦公軟件中查看和編輯。
2. 類似 Flyway 的命令管理，易於使用。
3. 可擴展的優先級算法。

## 安裝

1. 克隆倉庫：git clone <倉庫地址>
2. 創建虛擬環境：
```bash
virtualenv venv
.\venv\Scripts\activate
```
3. 安裝所需依賴：
```bash
pip install -r requirements.txt
```
4. 運行設置腳本（如果有）：
```bash
python setup.py install
```

## 第一步

- conf/ projects.json
您需要提供本月計劃的項目，Flyday 將為您安排每天的任務。

- conf/ project_tasks.json
您可以定義項目類型，每種類型包含特定的任務。任務可以定義可用的工作時數。

## 第二步

在 conf/config.json 中:

- priority_method: 提供兩種優先級算法。第一種是 LongestJobFirst，工時較長的項目具有更高的優先級。第二種是 AlternatingApproach，交替處理工時長短不一的項目集，以生成每日任務。這確保短期任務不會被過度延遲，適用於有突發休假或缺席的月份。默認設置為 AlternatingApproach。

- maxhours: 一天中的工作時數，以正整數表示。

- alternating_flag: 為 True 或 False，用於記錄目的。

## 使用方法

安裝後，您可以使用提供的指令來管理您的任務。

指令

- migrate
使用此指令生成基於每日優先級的工作計劃。

```bash
migrate
```

- info
提供工作計劃的當前狀態概覽。

```bash
info
```

- repair
如發現任務計劃有差異，使用此指令重新安排 projects.json 中的優先級。優先級將根據 remaining_hours 進行調整。

```bash
repair
```

- undo
如果您想回退 Schedule.csv，並備份新的 Schedule_bak.csv，使用此指令撤銷上一次任務遷移。

```bash
undo
```

## 許可證

根據 Apache License 分發。
