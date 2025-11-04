from arabic_reshaper import reshape
from bidi.algorithm import get_display
from termcolor import colored

right = colored('Right Answer', 'green')
wrong = colored('Wrong', 'red')

def reshaping(text):
    t = reshape(text)
    d = get_display(t)
    return d

class MainGame:
    def __init__(self, score = 0):
        self.score = score

    def data(self):
        return [
            {
                "Question": "ما هي عاصمة كندا",
                "Suggestion": ["تورونتو", "أوتاوا", "فانكوفر"],
                "RightAnswer": "أوتاوا"
            },
            {
                "Question": "من هو مؤلف رواية “الحرب والسلام”",
                "Suggestion": ["ليو تولستوي", "فيودور دوستويفسكي", "أنطون تشيخوف"],
                "RightAnswer": "ليو تولستوي"
            },
            {
                "Question": "كم عدد الألوان في قوس قزح",
                "Suggestion": ["5", "7", "9"],
                "RightAnswer": "7"
            },
            {
                "Question": "ما هو رمز عنصر الذهب في الجدول الدوري",
                "Suggestion": ["Au", "Ag", "Gd"],
                "RightAnswer": "Au"
            },
            {
                "Question": "من هو أول رجل هبط على سطح القمر",
                "Suggestion": ["نيل أرمسترونغ", "يوري جاجارين", "جون جلين"],
                "RightAnswer": "نيل أرمسترونغ"
            },
            {
                "Question": "أي كوكب هو الأقرب إلى الشمس",
                "Suggestion": ["الزهرة", "عطارد", "المريخ"],
                "RightAnswer": "عطارد"
            },
            {
                "Question": "كم عدد الدول الأعضاء في الأمم المتحدة",
                "Suggestion": ["193", "195", "200"],
                "RightAnswer": "193"
            },
            {
                "Question": "من هو صاحب لوحة “الموناليزا”",
                "Suggestion": ["فان جوخ", "ليوناردو دا فينشي", "بيكاسو"],
                "RightAnswer": "ليوناردو دا فينشي"
            },
            {
                "Question": "ما هي العملة الرسمية في اليابان",
                "Suggestion": ["الين", "اليوان", "الوون"],
                "RightAnswer": "الين"
            },
            {
                "Question": "ما هو أكبر محيط في العالم",
                "Suggestion": ["المحيط الأطلسي", "المحيط الهندي", "المحيط الهادئ"],
                "RightAnswer": "المحيط الهادئ"
            },
            {
                "Question": "من هو مكتشف قانون الجاذبية",
                "Suggestion": ["نيوتن", "أينشتاين", "كوبرنيكوس"],
                "RightAnswer": "نيوتن"
            },
            
            {
                "Question": "ما هي اللغة الرسمية في البرازيل",
                "Suggestion": ["الإسبانية", "البرتغالية", "الإنجليزية"],
                "RightAnswer": "البرتغالية"
            },
            {
                "Question": "كم عدد الكواكب في المجموعة الشمسية",
                "Suggestion": ["7", "8", "9"],
                "RightAnswer": "8"
            },
            {
                "Question": "ما هو الحيوان الوطني في أستراليا",
                "Suggestion": ["الكوالا", "الكنغر", "الإيمو"],
                "RightAnswer": "الكنغر"
            },
            {
                "Question": "ما هي أكبر قارة في العالم من حيث المساحة",
                "Suggestion": ["أمريكا الشمالية", "أفريقيا", "آسيا"],
                "RightAnswer": "آسيا"
            },
            {
                "Question": "ما هو العنصر الأكثر وفرة في الغلاف الجوي للأرض",
                "Suggestion": ["الأكسجين", "النيتروجين", "الهيليوم"],
                "RightAnswer": "النيتروجين"
            },
            {
                "Question": "أي من التالي هو حيوان بحري",
                "Suggestion": ["الفهد", "القرش", "النسر"],
                "RightAnswer": "القرش"
            },
            {
                "Question": "ما هي أكبر جزيرة في العالم؟",
                "Suggestion": ["أستراليا", "جرينلاند", "مدغشقر"],
                "RightAnswer": "جرينلاند"
            },
            {
                "Question": "ما هو اسم العلم الذي يدرس الصخور",
                "Suggestion": ["الجيولوجيا", "البيولوجيا", "الفلك"],
                "RightAnswer": "الجيولوجيا"
            },
            {
                "Question": "من هو أول رئيس للولايات المتحدة",
                "Suggestion": ["توماس جيفرسون", "جورج واشنطن", "أبراهام لنكولن"],
                "RightAnswer": "جورج واشنطن"
            }
        ]
    

    def Start(self):
        for i in range(0, 10):
            print('='*50)
            print(reshaping(MainGame().data()[i]['Question']))
            print('='*50)
            print('1 ->', reshaping(MainGame().data()[i]['Suggestion'][0]))
            print('2 ->', reshaping(MainGame().data()[i]['Suggestion'][1]))
            print('3 ->', reshaping(MainGame().data()[i]['Suggestion'][2]))
            choice = int(input('\nThe Right Answer Is : ')) - 1
            
            if MainGame().data()[i]['RightAnswer'] == MainGame().data()[i]['Suggestion'][choice]:
                self.score += 5000
                print(f'\n{right} Your Score Is {self.score} $\n')
            else:
                self.score -= 5000
                print(f'\n{wrong} !! >> The Right Answer Is -- {reshaping(MainGame().data()[i]['RightAnswer'])} --\n')
                print(f'Your Score Is {self.score} $\n')

MainGame().Start()