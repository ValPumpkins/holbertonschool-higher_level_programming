#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list == [] or my_list is None:
        return 0
    totalScore = 0
    totalWeight = 0

    for score, weight in my_list:
        totalScore += score * weight
        totalWeight += weight

    if totalWeight == 0:
        return 0

    return totalScore / totalWeight
