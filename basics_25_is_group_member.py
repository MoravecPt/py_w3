def is_group__member(group_data, n):
    for value in group_data:
        if n == value:
            return True
    return False
print(is_group__member([1,4,5,7],3))
print(is_group__member([1,4,5,7],4))