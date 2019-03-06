"""
罗马数字转整数
I 1, V 5, X 10, L 50, C 100, D 500, M 1000
一般每一位的罗马数字代表的数值相加
特例:
IV=4, IX=9,
XL=40, XC=90,
CD=400, CM=900,
"""
rms = 'CM'
def trans(r):
    if r == "I":
        return 1
    elif r == "V":
        return 5
    elif r == "X":
        return 10
    elif r == "L":
        return 50
    elif r == "C":
        return 100
    elif r == "D":
        return 500
    else:
        return 1000

def romanToInt(s):
    res = 0
    tmp = 0
    i = 0
    while i < len(s):
        i = i + 1
        if trans(s[-i]) > tmp:
            tmp = trans(s[-i])
            res = res + trans(s[-i])
        else:
            res = res - trans(s[-i])
    return res

print(romanToInt(rms))