import os, json, datetime
import phonenumbers 
from phonenumbers import carrier, geocoder, timezone

class Application:
    def __init__(self):
        pass
    def run(self):
        select = input(
            
'''
    ** Applications List:

    1 - Caller ID

    2 - Notebook (Coming Soon !!)

    3 - .......!!! (Comming Soon !!)

    ? - >> '''
    
    )
        if select == '1':
            Application().caller_id()

    def caller_id(self):
        phone = input(
'''
    ** Welcome To Caller ID App

    ** Description :

        caller id app contains useful functions that helps you to get carrier_name and display

        of any phone number

        to try the app follow the tip bellow
        
        TIP : Enter A Phone Number ( region code ex: +213 must be added first)
        
    **  Phone Number >> ''')

        parsed_number = phonenumbers.parse(phone, 'en')
        carrier_name = carrier.name_for_number(parsed_number, lang='en')
        tz = timezone.time_zones_for_geographical_number(parsed_number)
        geo = geocoder.country_name_for_number(parsed_number, lang='en')

        details = json.dumps([
                {
                    "PhoneNumber": phone,
                    "Carrier": carrier_name,
                    "TimeZone": tz,
                    "GeoCoder": geo
                }
            ], indent=4)
        
        print(details)

        with open('data\\phone_numbers.json', 'a') as f:
            f.write(details)
            
class AccountApp:
    def __init__(self) -> None:
        pass

    def login(self):
        with open('data\\profile.json', 'r') as f:
            loader = json.load(f)
            user = loader['username']
            time = datetime.datetime.now().strftime('%H:%M:%S')
            
           
       
            select = input(
f'''
================================ Welcome Back {user} ===============================

    ** Dashboard **                            ** Logged In Time : {time} **

    ** 1) Applications

    ** 2) Tools

    ** 3) Profile & Settings

    ** 4) Logged Out
    
    ** ?) >> ''')

        if select == '1': 
            Application().run()

        else:
            pass

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