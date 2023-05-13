#ループと条件分岐を使った適当なプログラム
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