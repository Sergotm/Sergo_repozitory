'//////////////////////////////////////////////////////////////   Регулярні вирази    ////////////////////////////////////////////////////////////////////////////////////'
import re

re.search(), 'виконує пошук першого входження шаблону в рядку.'
def search():
    '//////////////////////////////////////////////////Поиск от и до///////////////////////////////////////////////////////////////////////////'
    text = 'Hello gays, wat\'h is your name?'
    paterrn = r'w\w*\'h'
    match = re.search(paterrn,text, re.IGNORECASE)
    if match:
        print(f'Мы нашли: {match.group()}')
    else:
        print(f'Мы ничего не нашли:')

    match.span(), 'повертає кортеж, що містить початкову та кінцеву позиції збігу'
    match.string(), 'повертає рядок, переданий у функцію'
    match.group(), 'повертає частину рядка, в якому був збіг'

    '/////////////////////////////////////////////////Поиск указаного значения////////////////////////////////////////////////////////////////////////////'
    text = "Hello my name is Serhii"
    pattern = r'name'
    match = re.search(pattern, text)

    if match:
        print("Знайдено:", match.group())

    '//////////////////////////////////////////////////Поиск почты///////////////////////////////////////////////////////////////////////////'
    text = 'Hello gays, wat\'h is your email: novikatmospro@gmail.com ?'
    paterrn = r'(\w+)@(\w+\.\w+)'
    match = re.search(paterrn,text)

    if match:
        user_info = match.group(1)
        user_info_1 = match.group(2)
        print(f'Имя пользователя: {user_info}')
        print(f'Домен: {user_info_1}')
    else:
        print(f'Мы ничего не нашли:') 
search()

re.findall(), 'використовується для знаходження всіх входжень шаблону, заданого регулярним виразом, у заданому рядку, -> List'
def findall():
    '//////////////////////////////////////////Выборка d+ всех цыфр и создание списка с ними///////////////////////////////////////////////////////////////////////////'
    text = "сегодня дома сели на дорогу сидеть"
    pattern = r"с\d+"
    matches = re.findall(pattern, text)
    print(matches)
    '//////////////////////////////////////////Выборка c\w+ все слова начинающиеся на с ///////////////////////////////////////////////////////////////////////////'
    text = "сегодня дома сели на дорогу сидеть"
    pattern = r"с\w+"
    matches = re.findall(pattern, text)
    print(matches)
findall()

re.sub(), 'використовується для заміни входжень регулярного виразу'
def sub():
    '//////////////////////////////////////////Выборка [\.\:\;\!\,\-\_] удаляет знаки///////////////////////////////////////////////////////////////////////////'
    file_name = "Python - потужна, універсальна; мова!"
    pattern = r'[\.\:\;\!\,\-\_]'
    replacement = '@'
    formatted_name = re.sub(pattern, replacement, file_name)
    print(f'{formatted_name}')
    '//////////////////////////////////////////Выборка возводим номер телефона в дужки///////////////////////////////////////////////////////////////////////////'
    phone = """
    Михайло Куліш: 050-171-1634
    Вікторія Кущ: 063-134-1729
    Оксана Гавриленко: 068-234-5612
    """
    pattern = r"(\d{3})-(\d{3})-(\d{4})"
    replacement = r"[\1]-\2-\3"
    formatted_phone = re.sub(pattern, replacement, phone)
    print(formatted_phone)
sub()

re.split(), 'використовується для розбивання рядка за заданим регулярним виразом.'
def split():
    '//////////////////////////////////////////Выводит список всех слов в строке///////////////////////////////////////////////////////////////////////////'
    text = "Python - це проста, але потужна мова програмування."
    kolas = re.sub('[\-,]','',text)
    words = re.split("\s+", kolas)
    print(words)  # Виведе список слів у рядку
    '//////////////////////////////////////////Разделяет строку с помощю указаных символов///////////////////////////////////////////////////////////////////////////'
    text = "apple#banana!mango@orange;kiwi"
    pattern = r'[\#1!@;:]'
    words = re.split(pattern, text)
    print(words)  # Виведе список слів у рядку
split()

def Основні_компоненти_регулярних_виразів_включають():
    '''
    Літерали - Пряме відображення символів (наприклад, a, B, 1).
    Метасимволи -Символи, які мають спеціальне значення в регулярних виразах (наприклад, . (крапка) відповідає будь-якому символу).
    Квантифікатори - Визначають, скільки разів елемент повинен відповідати (наприклад * означає 0 або більше повторень).
    Класи символів - Визначають групи символів (наприклад, [a-z] відповідає будь-якій малій літері).
    Групи та діапазони - Використовуються для групування частин виразу (наприклад, (abc) визначає групу символів).
    Альтернації - Відповідає одному з декількох шаблонів (наприклад, a|b відповідає a або b).
    Якорі - Визначають позиції у тексті (наприклад, ^ для початку рядка, $ для кінця рядка).

    Прикладом блоку може бути:
    \w — будь-яка цифра або буква [a-zA-Z0-9_] (\W — все, крім букви або цифри [^a-za-z0-9_])
    \d — будь-яка цифра [0-9] (\D — усе, крім цифри [^0-9])
    \s — будь-який пробільний символ [\t\n\r\f\v] (\S — усе, крім пробільних символів [^\t\n\r\f\v])
    \b — межа слова
    [...] — один із символів у дужках ([^ ] — будь-який символ, крім тих, що в дужках)
    ^ i $ — початок i кінець рядка відповідно
    ( ) — групує вираз i повертає знайдений текст
    \t, \n, \r — символ табуляції, нового рядка та повернення каретки

    Модифікатори можуть вказувати на кількість повторень блоку у виразі, наприклад:

    . — один будь-який символ, крім рядка \n
    ? — 0 або 1 входження шаблону зліва
    + — 1 i більше входжень шаблону зліва
    * — 0 i більше входжень шаблону зліва
    \ — екранування спец.символів (приклад: \. — означає крапку або \+ — знак "плюс")
    {n} суворо n разів (n ціле число)
    {n,m} — від n до m входжень (приклад: {,m} — від 0 до m)
    a|b — відповідає a або b. Сам символ | означає "або" між двома шаблонами
    ( ) — групує вираз i повертає знайдений текст'''

def home():#'Тут будут идеи'
    count = 0
    text = "Контакти: Karina@example.com, Segorm@sample.org"
    pattern = r'\w+@\w+\.\w+'
    matches = re.findall(pattern, text)
    print(matches)
    for i in matches:
        new_pattern = r'(\w+)@(\w+\.\w+)'
        jet = re.search(new_pattern, matches[count])

        if jet:
            user_info_1 = jet.group(1)
            user_info_2 = jet.group(2)
            print(f'Имя пользователя: {user_info_1}')
            print(f'Домен: {user_info_2}')
            count +=1
home()

