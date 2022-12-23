lst = []

def print_lst(lst):
    if len(lst) != 0:
        lst.insert(-1, 'and')
        new_lst=(', '.join(lst))
        new_lstt = ''.join(new_lst.rsplit(',', 1))
        print(new_lstt)
    else:
        exit()
    
while True:
    print('Enter value for list ' + str(len(lst) + 1) + ' (Or press enter to stop.)')
    value = input()
    if value == '':
        break
    lst = lst + [value]

print_lst(lst)
