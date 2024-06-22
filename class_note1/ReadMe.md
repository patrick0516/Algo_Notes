## 查表法
用簡單翻譯系統做例子，參閱 e2c.py。

## 費氏數列 (Fibonacci sequence)
採用 recursion  
function: $F(n) = F(n-1) + F(n-2), (n>=3, n \in N)$  
參閱 fibonacci.py

## 改良
用查表法紀錄已經計算過的，避免 recursion 的重複計算，用空間換取費氏數列的時間。  
參閱 fibonacci_lookup.py

## C(n,k)
參閱 cnk.py

### [巴斯卡三角形](https://zh.wikipedia.org/zh-tw/杨辉三角形)
<img width="484" alt="image" src="https://github.com/patrick0516/Algo_Notes/assets/109636871/b538b253-0986-41b2-8e96-afef0bd936df">

### recursion 版
參閱 cnkR.py

根據巴斯卡定理的公式推演
$C_{m-1}^{n-1} + C_{m}^{n-1} = C_{m}^{n}$

解釋 [巴斯卡定理](https://tpdjdje0525.medium.com/%E5%B7%B4%E6%96%AF%E5%8D%A1%E5%AE%9A%E7%90%86-%E6%9C%89%E4%BB%80%E9%BA%BC%E6%84%8F%E7%BE%A9-21690183d2d1)
