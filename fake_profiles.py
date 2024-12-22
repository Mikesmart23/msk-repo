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
    
    print('**  Profiles-DataBase  **')
    print('_'*50)
    for index, profile in enumerate(range(len(profiles))):
        print('- Profile n :', index)
        print('_'*50)
        print('- name :', profiles[profile]['name'])
        print('- phone-number :', profiles[profile]['phone-number'])
        print('- email :', profiles[profile]['email'])
        print('- address :', profiles[profile]['address'])
        print('_'*50)

fakeProfiles()