def modify_list(item_list):
    new_list = item_list.copy()
    for i in range(len(new_list)):
        new_list[i] *= 2
    return new_list

numbers = [1, 2, 3, 4, 5]
modify_list(numbers)
print(numbers)