#与えられた2つのパラメーターの合計を2倍したものが60を超えているかどうか
def check_sum_2times_over_60(par1, par2):
    if (par1 + par2) * 2 > 60:
        print('over')
    else:
        print('safe')
    pass


#与えられた金額に消費税率8%を含めた値が5000を超えているかどうか。小数点は含めない
def tax_include(cost):
    a = cost * 1.08
    int(a)
    if a > 5000:
        print('safe')
    else:
        print('safe')
    pass


#与えられたスコアを80以上なら'A'、60以上80未満なら'B'、45以上60未満なら'C'、
#45未満は'F'と返す
def judge_rank(score):
    if score >= 80:
        print('A')
    elif 80 > score >= 60:
        print('B')
    elif 60 > score >=45:
        print('C')
    else:
        print('F')
    pass


#与えられた数値の階乗を返す。ただし再帰は使用禁止。
def factorial(num):
    b = 1
    for n in range(num):
        b *= n
    print(b)
    pass


#与えられた数値の2の累乗を返す。再帰使用禁止。便利な演算子使用禁止。
def power_of_two(num):
    print (2 ** num)
    pass


if __name__ == '__main__':
    check_sum_2times_over_60(15,16)
    tax_include(4321)
    judge_rank(91)
    factorial(100)
    power_of_two(3)
    pass
