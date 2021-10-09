# my_str = "blablacar"
# my_symbol = "bla"
# result = my_str.count(my_symbol)
# new_str = my_str.replace(my_symbol, '')
# result = (len(my_str) - len(new_str)) // len(my_symbol)
# print(result)

#######################

# my_str = "blablacar"
# my_symbol = "bla"
#
# my_symbol_count = my_str.count(my_symbol)

# result = f"{my_symbol}\n" * my_symbol_count
# result = result.strip()
# print(result)

# for my_count in range(my_symbol_count):
#     print(my_symbol)

##########################

# my_str = "bla BLA car"
# lower_str = my_str.lower()
# unique_symbols = []
#
# for symbol in lower_str:
#     if symbol not in unique_symbols:
#         unique_symbols.append(symbol)
# unique_symbols_count = len(unique_symbols)
# print(unique_symbols_count)

########################

# my_str = "qwertyuiopdfkflfl"
# my_list = []
# print(id(my_list), my_list)
# new_str = my_str[::2]
# # for symbol in new_str:
# #     my_list.append(symbol)
# my_list += list(new_str)
# print(id(my_list), my_list)

##################
# from string import ascii_lowercase as alphabet
#
# my_str = alphabet
# str_index = [7, 8, 11, 11, 4, 11]
# my_list = []
# for index in str_index:
#     symbol = my_str[index]
#     my_list.append(symbol)
# print(my_list)

##################
#
# number = 12345865318481911681105844892131689
#
# digit_count = len(str(number))
# print(digit_count)

###################

# number = 123458653184811168110584482131689
# max_symbol = max(str(number))
# print(max_symbol)

#####################

# number = 12345865318481911681105844892131689
# numb_str = str(number)
# numb_str = numb_str[::-1]
# result_number = int(numb_str)
#
# print(result_number)

################

# number = 12345865318481911681105844892131689
# numb_str = str(number)
# sort_numb_list = sorted(numb_str, reverse=True)
# new_number = "".join(sort_numb_list)
# result = int(new_number)
# print(result, new_number)

# my_list = [3, 6, 1, 8]
# y_list = sorted(reverse=True)
# my_list.sort(reverse=True)
#
# print(my_list)

##############

# my_list_1 = [1, 2, 3]
# my_list_2 = [10,20,30]
# my_result = []
#
# for index in range(len(my_list_1)):
#     # to_extend = [my_list_1[index], my_list_2[index]]
#     my_result.extend(my_list_1[index], my_list_2[index]])
#     my_result.append(my_list_1[index])
#     my_result.append(my_list_2[index])
# print(my_result)
#
# my_list_1 = [1, 2, 3]
# my_list_2 = [10, 20, 30]
# my_result = []
# min_len_lists = min(len(my_list_1), len(my_list_2|))
#
# tail = my_list_1[min_len_lists:]

######################################## ord and chr

# print(ord("b"))
# print(chr(75))

########################### генератор списков (list comprehension)

# alphabet_list = []
# for index_ascii in range(ord('a'), ord('z') + 1):
#     alphabet_list.append(chr(index_ascii))

# alphabet_list = [chr(index_ascii) for index_ascii in range(ord('a'), ord('z') + 1)]
# alphabet = "".join(alphabet_list)
# print(alphabet)
#
# result = [x ** 2 for x in range(10)]
# print(result)

#######

# my_list = [12, -45, 23, 5, 0, 21, 900]
# res = [str(value) * 20 for value in my_list if value > 10]
# res = []
# for value in my_list:
#     if value > 10:
#         res.append(value)
# [print(line) for line in res]
# for line in res:
#     print(line)

##### множества (set) - изменяемый тип, только один представитель для каждого объекта, порядок не сохраняется

# my_list = [1, 2, 3, 4, 5, 7, 6, 8, 9, '1']
#
# my_set = set(my_list)
# print(my_set, type(my_set))

#################

# my_str = "bla BLA car"
# lower_str = my_str.lower()
#
# unique_symbols_count = len(set(my_str.lower()))
# print(unique_symbols_count)

######
#
# my_list = [1, 2, 3, 4, 5, "7", 6, 8, 9, '1']        # убрать дубли
#
# my_list_unique = set(my_list)
# my_set = set(my_list)
# my_set.add(1000)
# print(my_set, type(my_set))

#########

# my_str_1 = "kenfkanekfnewkfwmlmflwkffkw"
# my_str_2 = "djwqnfkfportpgotormoemvefoeasdw"
#
# my_str_1_set = set(my_str_1)
# my_str_2_set = set(my_str_2)
#
# same_symbols = my_str_1_set.intersection(my_str_2_set)
# print(same_symbols)
#
# all_symbols = my_str_1_set.union(my_str_2_set)
# print(all_symbols)
#
# first_str_unique = my_str_2_set.difference(my_str_1_set)
# print(first_str_unique)