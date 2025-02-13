str_var : str = 'PyQonsole'

print(' <-> '.join(str_var.upper()).count('-'), )

print(*str_var, end=' Subscribe !!\n')

cheat = str_var.center(110).find('o')
if cheat:
    print('like the video - ' * (25//4))

print(str_var.count('Q'))

set_var = set(str_var)

print(set_var.symmetric_difference(list(str_var)))