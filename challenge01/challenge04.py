'''
2019/07/08
s19005 國吉 佑都
1つめの関数の戻り値を変数として保存し、２つめの関数の引数として渡す
'''
def div(x):
    return x // 2

def app(y):
    return y * 4

a = div(4)
print(app(a))
