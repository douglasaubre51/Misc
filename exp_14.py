list_1 = [ 10, 2,3, 5,3,1,5,3,2,54,6,3, 4, 5 ]
list_2 = [ 10, 2,3, 5,3,1,5,3,2,54,6,3, 4, 1 ]

tuple_1 = (123,1,321,3,5,6,0,1)
tuple_2 = (12,1,32,3,5,6,0,1)

set_1 = { "apple", "orange", "grapes", "pineapple"}
set_2 = { "apple", "pineapple"}

dict_1 = { }
dict_2 = {
        "allen" : 60,
        "alan ps" : 99,
        "lijo" : 50,
        "dibin" : 99
}

# lists

def find_largest_no():
    list_1.sort()
    print(f'largest no in list: {list_1[-1]}')

def remove_duplicate():
    list_1.sort()
    to_set = set(list_1)

    print(f'unique list: {to_set}')

def check_equal_list():
    if list_1 == list_2:
        print(f'{list_1} equal to {list_2}')
    else:
        print(f'{list_1} not equal to {list_2}')

def count_even_nums():
    count = 0

    for i in range(len(list_1)):
        if list_1[i] % 2 == 0:
            # print('even nos: ', list_1[i])
            count += 1

    print(f'even nums present: {count}')

# tuples

def min_max():
    print(f'min value: {min(tuple_1)}')
    print(f'max value: {max(tuple_1)}')

def sum():
    tuple_sum = 0

    for i in tuple_1:
        tuple_sum += i

    print(f'sum of elements: {tuple_sum}')

def union_inter_diff():
    print(f'union: {set_1.union(set_2)}')
    print(f'difference: {set_1.difference(set_2)}')
    print(f'intersection: {set_1.intersection(set_2)}')

def subset_superset():
    print(f'is {set_1} subset of {set_2}: {set_1.issubset(set_2)}')
    print(f'is {set_1} superset of {set_2}: {set_1.issuperset(set_2)}')


#dict

def add_students():
    name = input('enter student name: ')
    age = int(input('enter student age: '))
    
    dict_1[name] = age

def show_students():
    print(dict_1)

def calc_high_mark():
    max = 0

    for key in dict_2:
        if dict_2[key] > max:
            max = dict_2[key]

    for key in dict_2:
        if dict_2[key] == max:
            print(f'top scorer: {key}')



# find_largest_no()
# remove_duplicate()
# check_equal_list()
# count_even_nums()
# min_max()
# sum()
# union_inter_diff()
# subset_superset()
#add_students()
#add_students()
#add_students()
#show_students()

calc_high_mark()
