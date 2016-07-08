#与えられた2つのパラメーターの合計を2倍したものが60を超えているかどうか
def check_sum_2times_over_60(par1, par2):
    return (par1 + par2) * 2 > 60


#与えられた金額に消費税率8%を含めた値が5000を超えているかどうか。小数点は含めない
def tax_include(cost):
    return cost * 1.08 > 5000

#与えられたスコアを80以上なら'A'、60以上80未満なら'B'、45以上60未満なら'C'、
#45未満は'F'と返す
def judge_rank(score):
    if score < 45:
        return 'F'
    if score < 60:
        return 'C'
    if score < 80:
        return 'B'
    return 'A'

#与えられた数値の階乗を返す。ただし再帰は使用禁止。
def factorial(num):
    total = 1
    for i in range(num, 1, -1):
        total *= i
    return total

#与えられた数値の2の累乗を返す。再帰使用禁止。便利な演算子使用禁止。
def power_of_two(num):
    total = 1
    for i in range(num):
        total *= 2
    return total

if __name__ == '__main__':
    print(check_sum_2times_over_60(15,16))
    print(tax_include(4321))
    print(judge_rank(91))
    print(factorial(100))
    print(power_of_two(3))
    pass
