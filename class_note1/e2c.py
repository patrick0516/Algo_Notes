import sys

e2c = {'dog':'狗', 'cat':'貓', 'a': '一隻', 'chase':'追', 'eat':'吃'}

def mt(elist):
    clist = []
    for e in elist:
        c = e2c[e]             # 檢查有沒有要找的單字
        clist.append(c)        # 有就 append 進 clist
    return clist

clist = mt(sys.argv[1:])       # 從第2元素開始，忽略腳本名稱
print(clist)
