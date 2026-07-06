def doc(*num):
    """ this function responsible for calculation sum of providing numbers """
    sum = 0
    for i in num:
        sum = sum + i
    return sum


print(doc(2,3,4,5,6,7))

print(doc.__doc__)