import os, json, datetime


class AccountApp:
    def __init__(self) -> None:
        pass

    def login(self):
        with open('data\\profile.json', 'r') as f:
            loader = json.load(f)
            user = loader['username']
            time = datetime.datetime.now().strftime('%H:%M:%S')
            
           
       
            print(
f'''
===================== Welcome Back {user} ==========================

    ** Dashboard **                            {time} 






''')

    def signin(self):
        first_name = input('\n* First Name * -> ')
        last_name = input('\n* last Name * -> ')
        user_name = input('\n* User Name * -> ')
        password = input('\n* Password * -> ')
        cnfrm_password = input('\n* Confirm Password * -> ')

        os.mkdir('data')
        with open('data\\profile.json', 'w') as f:
            f.write(json.dumps({
                "firstname": first_name,
                "lastname": last_name,
                "username": user_name,
                "password": password
            }, indent=4))

        
    def home_page(self):
        select = input(
'''
====================== Welcome To Your Store ===================

=== For More Description Open Readme.txt File

=== Hints :

=== 1) SIGN IN >> Command ( sign )

=== 2) LOG IN >> Command ( log )

=== 3) QUIT >> Command ( q )

=== >> ''')
        print('\n==========================================================================')

        if select == 'sign':
            AccountApp().signin()
            AccountApp().login()

        elif select == 'log':
            AccountApp().login()

AccountApp().home_page()