
class ChatBot:
    def __init__(self):
        pass
    def run(self):
        bot = [
            'Welcome User, Enter Your Name To Comunicate Better :',
            'OK , How Can I Help You ?',
            'So, Your Name Ali 🙄 ??',
            'Sorry, I Made A Mistake Forgive Man !! ',
            'Tell Me About Yourself',
            'They Calls Me Stupid Bot Is That Right ?',
            'How Old Are You ??',
            'Do You Have A Hobby ??',
            'Im Advicing You For Doing Some Sport And Healthy Food For Better Well'
        ]
        for question in bot:
            print('\n- Bot >>', question)
            user_requests = input('\n- You >> ')
            

ChatBot().run()
