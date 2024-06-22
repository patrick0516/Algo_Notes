## 查表法
用簡單翻譯系統做例子，參閱 e2c.py。

## 費氏數列 (Fibonacci sequence)
採用 recursion  
function: $F(n) = F(n-1) + F(n-2), (n>=3, n \in N)$  
參閱 fibonacci.py
## 改良
用查表法紀錄已經計算過的，避免 recursion 的重複計算，用空間換取費氏數列的時間。  
參閱 fibonacci_lookup.py
