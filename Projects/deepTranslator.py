from deep_translator.google import GoogleTranslator
from arabic_reshaper import reshape
from bidi.algorithm import get_display

def reshapArabic(text):
    string_= reshape(text=text)
    display = get_display(string_)
    return display

class Translator:
    def __init__(self):
        select = input(
'''
_______________________________________________________________

Command Line Translator Using DeepTranslator Library Framework  
_______________________________________________________________

Translate To :

1 - English -> from ( Auto Detect ) - to ("en" -> English )

2 - Arabic -> from( Auto Detect ) - to ("ar" -> Arabic)

3 - French -> from ( Auto Detect ) - to ("fr" -> French)

4 - Spanish -> from ( Auto Detect ) - to ("es" -> Spanish)

? - Hint : Select Translation Methode By Its Index Bellow :

    # - ''' )

        self.string = input('\n- Enter A Text To Translate : ')

        if select == '1':
            self.to_english()
        elif select == '2':
            self.to_arabic()
        elif select == '3':
            self.to_french()
        elif select == '4':
            self.to_spanish()
    

    def to_english(self):
        translate = GoogleTranslator().translate(self.string)
        print('\n- Result : ', translate)

    def to_arabic(self):
        translate = GoogleTranslator(source='auto', target='ar').translate(self.string)
        print('\n- Result : ', reshapArabic(translate))


    def to_spanish(self):
        translate = GoogleTranslator(source='auto', target='es').translate(self.string)
        print('\n- Result : ', translate)

    def to_french(self):
        translate = GoogleTranslator(source='auto', target='fr').translate(self.string)
        print('\n- Result : ', translate)

Translator()



