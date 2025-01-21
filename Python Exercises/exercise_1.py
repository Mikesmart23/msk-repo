
items = ['python', 24, [8, 12], 5]
items[2] = [14, 5]; x = items[1] - 10 ; y = items[2][0]
# x = 14 , y = 14
if items[0].startswith('p') and items[-1] % 2 == 0:
    # True and False => False
    if x < items[-1] or x + 10 == items[1]:
        # x = 14 , items[-1] = 5 False or x + 10 = 24 == 24 True
        print('partial if statment is true')
    else:
        print('partial else statment')
# elif 
else:
    if 'th' in items[0] and y*2 < items[-1] + 20:
        # True and (28 < 25) -> False
        print('partial if of else statment')
    else:
        print('partial else of else statment')