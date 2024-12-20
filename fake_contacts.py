from faker import Faker

def contacts():
    contacts = [
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
    print('_'*50)
    print('**  My-Contacts  **')
    print('_'*50)
    for index, profile in enumerate(range(len(contacts))):
        print('- contact n :', index)
        print('- name :', contacts[profile]['name'])
        print('- phone-number :', contacts[profile]['phone-number'])
        print('- email :', contacts[profile]['email'])
        print('- address :', contacts[profile]['address'])
        print('_'*50)

contacts()