#coding:utf-8

"""
1 ~ 100までの整数
3で割り切れるものはFizz
5で割り切れるものはBuzz
両方はFizz Buzz
"""

str_n = ""
for i in range(1 , 101):
    if i == 1:
        str_n += "%d" % i
    elif i % 15 == 0:
        str_n += ", Fizz Buzz"
    elif i % 5 == 0:
        str_n += ", Buzz"
    elif i % 3 == 0:
        str_n += ", Fizz"
    else:
        str_n += ", %d" % i

print str_n

