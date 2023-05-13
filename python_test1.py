#ループと条件分岐を使ったプログラム
'''
ダブルクォーテーション(")やシングルクォーテーション(')を３つ連続することで後ろにさらに３つ追加補完される
その間にかかれたコードはすべてコメントアウトされる。
extension(拡張機能):autoDocstring
'''
def test():
    fruit_list = ["apple","banana","grape","strawberry"]
    for value in fruit_list:
        if value == "apple" or value == "strawberry":
            print("赤い果物")
        elif value == "banana":
            print("黄色い果物")
        else :
            print("赤色でも黄色でもない果物")

test()