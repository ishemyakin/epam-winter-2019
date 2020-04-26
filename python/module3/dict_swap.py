def dict_swap(dict1):
    print(dict1.get('John'))
    print(dict1.items())
    print(dict1.values())
    dict2 = {dict1[name]: name for name in dict1}
    return dict2


a = {'John': 'Name', 44: 'Age', 'DevOps': "JobTitle"}
dict_swap(a)
