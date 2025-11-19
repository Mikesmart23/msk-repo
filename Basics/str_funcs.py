# string functions full tutorial ..

myName = "i'm PyQonsole !!"

####################### 1. Modification Methods ######################                      

# Capitalizes the first character of the string
# كتابة الحرف الأول بحرف كبير 
print(myName.capitalize())

# Converts the first character of each word to uppercase and the rest to lowercase
# كتابة الحرف الأول من كل كلمة بحرف كبير 
print(myName.title())

# Converts all characters to uppercase
# تحويل جميع الأحرف إلى أحرف كبيرة 
print(myName.upper())

# Converts all characters to lowercase
# يحول جميع الأحرف إلى أحرف صغيرة 
print(myName.lower())

''' Converts the string to lowercase, more aggressive than lower() for 
    case-insensitivity comparisons'''
#  تحويل إلى أحرف صغيرة للمقارنات غير الحساسة لحالة الأحرف 
print(myName.casefold())

# Swaps the case of all characters in the string
# تبديل الأحرف الكبيرة والصغيرة 
print(myName.swapcase())

''' Centers the string in a field of given width, padded with fillchar
    (default is space)'''
# يقوم بمركز السلسلة في حقل بعرض معين، مع تعبئة الأحرف (الافتراضي هو المسافة) 
print(myName.center(20, '-'))

# Formats the string using placeholders
# تنسيق السلسلة باستخدام العناصر النائبة 
print("PyQonsole is {}".format('Awesome !!'))

##################################################################
####################### 2. Whitespace Methods ######################

# Removes leading characters (whitespace by default)
# إزالة الأحرف الرئيسية (المسافة البيضاء افتراضيًا) 
print('    PyQonsole'.lstrip())

# Removes trailing characters (whitespace by default)
# إزالة الأحرف الزائدة (المسافة البيضاء افتراضيًا) 
print("Hello, Python        ".rstrip())

# Removes leading and trailing whitespace
# يزيل المسافات البيضاء البادئة واللاحقة 
print('    Py    '.strip())
###############################################################################
####################### 3. Searching and Finding Methods ######################

# Returns the lowest index of the substring if found, else returns -1
# إرجاع أدنى مؤشر للسلسلة الفرعية إذا تم العثور عليها، وإلا يتم إرجاع -1 
print(myName.find('!'))

# Returns the highest index of the substring if found, else -1.
# إرجاع أعلى مؤشر للسلسلة الفرعية إذا تم العثور عليها، وإلا -1 
print(myName.rfind('o'))

# Similar to find(), but raises a ValueError if the substring is not found.
# مشابه لـ find()، لكنه يثير ValueError إذا لم يتم العثور على السلسلة الفرعية 
print(myName.index("Q"))

# Like rfind(), but raises a ValueError if the substring is not found
# مثل rfind()، لكنه يثير ValueError إذا لم يتم العثور على السلسلة الفرعية 
print(myName.rindex('!'))

# Counts occurrences of a substring in the string
# يحسب عدد مرات ظهور سلسلة فرعية في السلسلة 
print(myName.count('o'))

###############################################################################
####################### 4. Splitting and Joining Methods ######################

# Splits the string into a list of substrings
# تقسيم السلسلة إلى قائمة من السلاسل الفرعية 
print("hello Python".split(" "))

# Splits the string from the right. If maxsplit is specified, it limits the number of splits
# يقسم السلسلة من اليمين. إذا تم تحديد maxsplit، فسيتم تحديد عدد التقسيمات 
print('py-qonsole'.rsplit('-', 1))

# Splits the string at line breaks, returning a list of lines
# تقسيم السلسلة عند فواصل الأسطر، وإرجاع قائمة من الأسطر 
print('hello\nPython'.splitlines())

'''Joins elements of an iterable into a single string
   using the string as a separator'''
# يربط عناصر قابلة للتكرار في سلسلة واحدة باستخدام السلسلة كفاصل 
print('*'.join(['PyQonsole', 'is', 'A', 'Programmer']))

##################################################################
####################### 5. Testing Methods ######################

# Returns True if all characters are alphanumeric
# يعود صحيحًا إذا كانت جميع الأحرف أبجدية رقمية 
print(myName.isalnum())

# Returns True if all characters in the string are alphabetic
# يعود صحيحًا إذا كانت جميع الأحرف في السلسلة أبجدية 
print(myName.isalpha())

# Returns True if all characters in the string are ASCII
# يعود صحيحًا إذا كانت جميع الأحرف في السلسلة عبارة عن ASCII 
print(myName.isascii())

# Returns True if all characters in the string are digits
# يعود صحيحًا إذا كانت جميع الأحرف في السلسلة أرقامًا 
print(myName.isdigit())

# Returns True if all cased characters are lowercase
# يعود صحيحًا إذا كانت جميع الأحرف الصغيرة صغيرة 
print(myName.islower())

# Returns True if all cased characters are uppercase
# يعود صحيحًا إذا كانت جميع الأحرف الكبيرة كبيرة 
print(myName.isupper())

# Returns True if all characters in the string are whitespace
# يعود صحيحًا إذا كانت جميع الأحرف في السلسلة عبارة عن مسافات بيضاء 
print(myName.isspace())

# True if the string starts with the specified prefix, otherwise False.
# صحيح إذا كانت السلسلة تبدأ بالبادئة المحددة، وإلا فهي خطأ 
print(myName.startswith('P'))

# Checks if the string ends with the specified suffix
# التحقق مما إذا كانت السلسلة تنتهي باللاحقة المحددة 
print(myName.endswith('le'))

###################################################################################
####################### 6.  Encoding and Translation Methods ######################

# Encodes the string using the specified encoding
# يقوم بترميز السلسلة باستخدام الترميز المحدد 
print(myName.encode())

# Creates a translation table
# إنشاء جدول ترجمة 
newName = myName.maketrans('tyQs5', 'pyqT6')
print('sython'.translate(newName))
#################################################################################
####################### 7. Replacing and Modifying Methods ######################

# Replaces occurrences of a substring with another substring
print(myName.replace('!!', '??'))

# Expands tabs in the string to spaces
# توسيع علامات التبويب في السلسلة إلى مسافات 
print("Py\tQonsole".expandtabs(4))

# Pads the string on the left with zeros to fill the specified width
# يملأ السلسلة الموجودة على اليسار بالأصفار لملء العرض المحدد 
print('10'.zfill(10))
##################################################################
###################### 8. Partitioning Methods ######################

# Splits the string at the first occurrence of the separator
# تقسيم السلسلة عند أول ظهور للفاصل 
print('Py*Qonsole'.partition('*'))

# Splits from the right side similar to partition().
# انقسامات من الجانب الأيمن مشابهة لـ partition() 
print('Py*Qonsole'.rpartition('*'))

##################################################################




