#coding:utf-8

import math

def sign(num):  # * の数を計算
    sum_n = 0
    str_n = str(num)
    for i in str_n:
        sum_n += int(i)
    return sum_n

def factorization(num): # 素因数分解
    list = []
    for i in range(2, int(math.ceil(num/2))):
        while True:
            if num % i != 0:
                break
            num /= i
            list.append(i)
    return list

def expression(list):   # 数式化
    ex_str = ""
    for i in range(len(list)):
        if i == 0:
            ex_str += "%s" % list[i]
        else:
            ex_str += " * %s" % list[i]
    return ex_str

def check(min, max):    # 
    for i in range(min, max):
        num = factorization(i)
        sign_n = sign(i)
        if len(num) - 1 == sign_n:
            ex_str = expression(num)
            print "%d(%d) = " % (i, sign_n) + ex_str

if __name__ == "__main__":
    ran_min = raw_input("range_minimum? >> ")
    ran_max = raw_input("range_maximum? >> ")
    check(int(ran_min), int(ran_max))
