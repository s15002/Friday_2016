#画面に自分の「学科名」「学年」「学生記番号」を出力

def print_self_infomation():
    print('ITスペシャリスト科、' + '1年生、' + 's15002')

    pass

#自分の年齢が、80歳になるまで後何年か計算をして出力

def print_how_many_years_to_80():
    print (80 - 26)
    pass

#与えられたパラメーターが「偶数」か「奇数」かを出力
def print_odd_or_even(target):
    a = 2
    if(a % 2 = 0){
        print('奇数')
    }else{
        print('偶数')
    }
    pass

#randomモジュールを使用して0-50の整数を生成し、25が出るまで「hoge」と出力
def print_hoge():
    #randint(0, 50)で、0-50の範囲から整数乱数を生成する
    from random import randint

    pass

#100から1000までの偶数のみを表示してください
def print_even_from_100_to_1000():
    pass

if __name__ == '__main__':
    print_self_infomation()
    print_how_many_years_to_80()
    print_odd_or_even(10)
    print_odd_or_even(13)
    print_hoge()
    print_even_from_100_to_1000()

    pass