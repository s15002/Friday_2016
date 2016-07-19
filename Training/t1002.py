import math

def cal(year, month):
    h = round (year / 100)
    y = year % 100
    m = month

    if year < 1000:
        h = math.floor((year / 100) * 10)
        y = year & 10
    if year == 1:
        m = 13
        u = y - 1
    elif month == 2:
        m  = 14
        y  = y - 1

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap_year = 29
            else:
                leap_year = 28
        else:
            leap_year = 29
    else:
        leap_year = 28

    if month == 4 or month == 6 or month == 9 or  month == 11:
        numberOfdays = 30
    elif month == 2 and  leap_year == 29:
        numberOfdays = 29
    elif month == 2 and leap_year == 28:
        numberOfdays = 28
    else:
        numberOfdays = 31

    W = (y + math.floor(y / 4) + math.floor(h / 4) - 2 * h + math.floor(13 * (m + 1) / 5) + 1) % 7 - 1
    if W == -1:
        W = 6
    num1 == 0
    num2 == 0
    num3 == 0
    num4 == 0
    num5 == 0
    i = 0
    list = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]

    for x in range(0, numberOfDays):
        if list1[0][6] == 0:
            i += 1
            list1[0][W] = i
            W += 1
        elif list1[0][6] != 0 and list1[1][6] == 0:
            i += 1
            list1[1][num1] = i
            num1 += 1
        elif list1[1][6] != 0 and list1[2][6] == 0:
            i += 1
            list1[2][num2] = i
            num2 += 1
        elif list1[2][6] != 0 and list1[3][6] == 0:
            i += 1
            list1[3][num3] = i
            num3 += 1
        elif list1[3][6] != 0 and list1[4][6] == 0:
            i += 1
            list1[4][num4] = i
            num4 += 1
            if i == numberOfDays:
                del list1[5]

            elif list1[4][6] != 0 and list1[5][6] == 0:
                i += 1
                list1[5][num5] = i
                num5 += 1

    return (list1)

if __name__ == '__main__':
    cal(2016, 8)