def print_params(a = 1, b = 'string', c = True):
    print(a, b, c)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [3, 'str', False]
values_dict = {'a' : 2, 'b' : 3, 'c' : 4}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = 2, 'str'

print_params(*values_list_2, 42)