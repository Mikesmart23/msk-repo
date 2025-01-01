from faker import Faker


def fakeProfiles():
    profiles = [
        {
            'name': Faker().name(),
            'phone-number': Faker().phone_number(),
            'email': Faker().email(),
            'address': Faker().address()
        },
                {
            'name': Faker().name(),
            'phone-number': Faker().phone_number(),
            'email': Faker().email(),
            'address': Faker().address()
        },
                {
            'name': Faker().name(),
            'phone-number': Faker().phone_number(),
            'email': Faker().email(),
            'address': Faker().address()
        },
                {
            'name': Faker().name(),
            'phone-number': Faker().phone_number(),
            'email': Faker().email(),
            'address': Faker().address()
        },
    ]
    print('** Profiles-DataBase **')
    print('_'*50)
    for index, profile in enumerate(range(len(profiles))):
        print(
f'''
    Profile N: {index}
    _________________________

    - Name : {profiles[profile]['name']}

    - Phone-Number : {profiles[profile]['phone-number']}

    - Email : {profiles[profile]['email']}

    - Address : {profiles[profile]['address']}

''')

fakeProfiles()