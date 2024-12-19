
class ChatBot:
    def __init__(self):
        pass
    def run(self):
        bot = [
            'Welcome User, Enter Your Name To Comunicate Better :',
            'How Old Are You ??',
            'OK , How Can I Help You ?',
            'Tell Me About Yourself',
            'Do You Have A Hobby ??',
            'Im Advicing You For Doing Some Sport And Healthy Food For Better Well'
        ]
        for question in bot:
            print('\n- Bot >>', question)
            user_requests = input('\n- You >> ')
            

ChatBot().run()
