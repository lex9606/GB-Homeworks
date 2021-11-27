new_list = input('Insert numbers with spaces: ').split()
for i in range(1, len(new_list), 2):
    new_list.insert(i - 1, new_list.pop(i))
    print(new_list)
