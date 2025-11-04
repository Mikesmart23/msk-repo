def mins_to_secs(value):
    print('Convert Minutes To Seconds\n')
    if value == 0:
        raise "value should't be zero '0' "
    return f'{value} minutes =>  {value * 60} seconds'

def hours_to_secs(value):
    print('Convert Hours To Seconds\n')
    if value == 0:
        raise "value should't be zero '0' "
    return f'{value} hours =>  {value * 3600} seconds'

def days_to_secs(value):
    print('Convert Days To Seconds\n')
    if value == 0:
        raise "value should't be zero '0' "
    return f'{value} days =>  {value * (3600 * 24) } seconds'

def weeks_to_secs(value):
    print('Convert Weeks To Seconds\n')
    if value == 0:
        raise "value should't be zero '0' "
    return f'{value} Weeks =>  {value * (3600 * 24 * 7) } seconds'

def months_to_secs(value):
    print('Convert Months To Seconds\n')
    if value == 0:
        raise "value should't be zero '0' "
    return f'{value} Months =>  {value * (3600 * 24 * 30) } seconds'

def years_to_secs(value):
    print('Convert Years To Seconds\n')
    if value == 0:
        raise "value should't be zero '0' "
    return f'{value} Years =>  {value * (3600 * 24 * 365) } seconds'


if __name__ == '__main__':
    print(f'{years_to_secs(0)}')