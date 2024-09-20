#!/usr/bin/python3
''' Change comes from within'''


def makeChange(coins, total):
    '''returs the fewest number of coins needed to meet 
    a given amount of coins'''
    if total <= 0:
        return 0
    coin = 0
    remain = total
    index = 0
    slc = sorted(coins, reverse=True)
    n = len(coins)
    while remain > 0:
        if index >= n:
            return -1
        if remain - slc[index] >= 0:
            remain -= slc[index]
            coin += 1
        else:
            index += 1

    return coin
