python setup.py install



pip freeze > requirements.txt



deactivate



venv\Scripts\activate

## 打包
1. D:\REPO_PY\flyday\env\Scripts  activate.bat
2. python setup.py build

1. 限制性SJF（又稱帶有過期時間的SJF）
這是SJF的一個變種，在這個策略中，會考慮任務的緊急程度。任務可能會有一個截止日期，而接近截止日期的任務會被賦予更高的優先級，即使它們不是最短的任務。

2. 艾森豪威爾矩陣（Eisenhower Matrix）
這種方法將任務分為四個類別：緊急且重要、重要但不緊急、緊急但不重要、既不緊急也不重要。你可以優先處理緊急且重要的任務，然後是重要但不緊急的任務。這可以幫助平衡緊迫性和重要性。

3. 交替法（Alternating Approach）
這個策略涉及交替處理一個長任務和一個短任務。這樣，你可以保持進度，同時確保長任務不會被推遲太久。

4. 限時任務優先（Deadline First Approach）
如果任務有明確的截止日期，你可以根據截止日期的迫切性來優先處理任務。任務越接近截止日期，優先級越高。

5. 動態優先權調整（Dynamic Priority Adjustment）
在這種方法中，任務的優先級會根據等待時間來動態調整。如果一個任務等待了很長時間，其優先級會增加，以防止它被忽略。

6. 優先級與成本/效益分析相結合
在這種策略下，對任務進行優先級排列時，會考慮每個任務的成本/效益比。這意味著，如果完成一個任務所帶來的效益遠大於其它任務，即使它不是最短或最緊急的，它也可能被賦予更高的優先權。

7. 長時間優先(Longest Job First)