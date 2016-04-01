# coding: utf-8

import math
import sys


def get_prime_list(total):
    """
    获取素数的列表

    :param total: 素数个数
    :return: 素数的列表
    """
    list_prime = []
    count = 0
    for i in xrange(2, 1000):
        is_prime = True
        end = int(math.sqrt(i)) + 1
        for j in xrange(2, end):
            if i % j == 0:
                is_prime = False

        if is_prime:
            list_prime.append(i)
            count += 1
            if count == total:
                break

    return list_prime


def get_char_prime(list_prime):
    """
    获取字符跟素数的映射表

    :param list_prime: 素数表
    :return: 字符素数表
    """
    char_prime = {}
    if len(list_prime) < 52:
        return None

    for i in xrange(65, 91):
        char_prime[chr(i)] = list_prime.pop(0)

    for j in xrange(97, 123):
        char_prime[chr(j)] = list_prime.pop(0)

    return char_prime


def get_value(string, char_prime):
    """
    获取字符串的值

    :param string: 字符串
    :param char_prime: 字符素数表
    :return: 素数相乘的值
    """
    num = 1
    for i in string:
        num *= char_prime[i] if i in char_prime else 1

    return num


def main():
    list_prime = get_prime_list(52)
    char_prime = get_char_prime(list_prime)
    if char_prime is None:
        print 'char_prime is None, System Exit'
        sys.exit(0)

    print char_prime

    string_1 = 'abasdsaefqwwerlasldfnAADAABADFADldfalnflkasndflkansdflkjaslfdsadfasdfasfas'
    value_1 = get_value(string_1, char_prime)
    print string_1, " : ", value_1

    string_2 = 'abefqlAD'
    value_2 = get_value(string_2, char_prime)
    print string_2, " : ", value_2

    string_3 = 'abefqlAC'
    value_3 = get_value(string_3, char_prime)
    print string_3, " : ", value_3

    if value_1 % value_2 == 0:
        print 'string_1 contains string_2'
    else:
        print 'string_1 not contains string_2'

    if value_1 % value_3 == 0:
        print 'string_1 contains string_3'
    else:
        print 'string_1 not contains string_3'

if __name__ == '__main__':
    main()
