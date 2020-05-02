def multiple_in_range(arg1, arg2):
    res = []
    for i in range(arg1, arg2+1):
        if i%7 == 0 and i%5 != 0:
            res.append(i)
    return res

# a = multiple_in_range(1, 219)
# print(a)
