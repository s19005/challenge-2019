'''
2019/07/10
s19005 國吉 佑都
文字列をfloat型に変換して戻り値とする関数
例外処理付き
'''
def flo():
    x = input()
    return float(x)

try:
    print(flo())
except ValueError:
    print('Invalid input')
