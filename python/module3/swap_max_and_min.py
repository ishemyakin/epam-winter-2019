def swap_max_and_min(kek_list):
    print(kek_list)
    lul_list = set(kek_list)
    print(lul_list)
    in_list = list(lul_list)
    if kek_list == in_list:
        print(in_list)
        # if "asd" in in_list:
        #     print('kek')
        # if "asd" in in_list:
        #     print('swap_max_and_min([-78, "asd", -50])')

        list_min = min(in_list)
        list_max = max(in_list)

        list_min_pos = in_list.index(list_min)
        list_max_pos = in_list.index(list_max)

        in_list[list_min_pos] = list_max
        in_list[list_max_pos] = list_min
    else:



# except (ValueError):
#     print("swap_max_and_min([43, 43, -50])")
# print("swap_max_and_min([-78, "asd", -50])")
# alpha_list = [1, 2, 3]
# kek = swap_max_and_min(alpha_list)
# print(kek)

# try:
#     swap_max_and_min([43, 43, -50])
#
# except TypeError as err:
#     print(f'TypeError + {err}')
#     pass
# except ValueError as err:
#     print(f'ValueError + {err}')
a = swap_max_and_min([43, 43, -50])
print(a)
