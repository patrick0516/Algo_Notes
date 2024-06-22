from datetime import datetime

def fibonacci (n):
    if n < 0: raise
    if n == 0: return 0
    if n == 1: return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# n = 10
# n = 40    # 要花將近 35 秒
n = 60      # 60 開始幾乎就很難跑完了
startTime = datetime.now()
print(f'fibonacci({n})={fibonacci(n)}')
endTime = datetime.now()
seconds = endTime - startTime
print(f'time:{seconds}')
