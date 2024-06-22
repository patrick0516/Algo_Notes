from datetime import datetime
fib = [None]*10000
fib[0] = 0
fib[1] = 1

def fibonacci(n):
    if n < 0: raise                                 # 檢查異常
    if not fib[n] is None: return fib[n]            # 如果已經計算過，直接 reyturn value。
    fib[n] = fibonacci(n - 1) + fibonacci(n - 2)    # 還是有 recursion。
    return fib[n]

# n = 35
n = 60
startTime = datetime.now()
print(f'fibonacci({n})={fibonacci(n)}')
endTime = datetime.now()
seconds = endTime - startTime
print(f'time:{seconds}')
