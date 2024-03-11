from pathlib import Path
with open('Python_Core\File\\text.txt', 'w', encoding='UTF-8') as file: # With гарантирует что файл будет закрыт как только мы выйдем с него \ as означает что мы вернем что-то в file
    file.write('Hello my name is Serhii'), 'Записываем в файл'

    file.seek(5), 'От куда начинаем выводить '
    lines = file.tell(), 'Поиск позиции курсора в этот моент в тексте '
    print(lines)

    read = file.read(), 'Выводим на екран текст'
    symbol = file.readline(), 'Читаем файл по строчно'
    symbol = file.readlines(), 'Читаем файл полностю и возвращаем список где 1 елемент это одна строка(\n Надо удаялять самостоятельно)'
    lines = [el.strip() for el in file.readlines()], 'Функция которая удаляет изсписка переноc\Пробелы на новую строку'
    
with open('Python_Core\File\\text.txt', 'r', encoding='UTF-8') as file:
    print(file.read(2)), 'Выводим на екран первых 2 значания'

    lines = [el.strip() for el in file.readlines()]
    print(lines)

'//////////////////////////////////////////////////////////////////////////       Bytes      ///////////////////////////////////////////////////////////////////////////////////////////////////////'
def bytes(): # Тут будут Bytes in the file
    
    file.write(b'Hello world!')
    'В этом режиме писать только Байт-строки или Байт-масивы'
    'Щоб працювати з послідовністю байтів у Python є вбудовані типи даних байт-рядків'
    bytes - 'незмінний тип, що використовують для представлення байтів'
    bytearray - 'змінний тип, що дозволяє модифікувати байти після їх створення'

    s = 'Hello world!'.encode(encoding='Тут метод кодировки',errors='Как обробляем ошибки') ,'-> Str -> Bytes | Изменяем строку на строку Bytes'
    '''encoding - вказує метод кодування. По замовчуванню використовується 'utf-8',\
        який підтримує велику кількість символів з різних мов.

    errors - вказує, як обробляти помилки кодування. Наприклад, 'strict' для викидання виключення у випадку помилки,\
        'ignore' для ігнорування помилок або 'replace' для заміни неможливих для кодування символів на певний замінник (?)'''
    s= hex(123,127,156), 'Представление числа в 16-цатой форме/ 0x  указывают на 16-форму'


    file_path = Path('Python_Core/Module/Pack/example.bin')
    data_bin = b'Python landguage class'
    file_path.write_bytes(data=data_bin)

    read_bytes = file_path.read_bytes()
    print(read_bytes)




    
def ASCII_UTF_8_CP1251(): # Котдировка строк
    '''Текст, що складається тільки з символів, коди яких менші ніж 128, при записі в UTF-8 перетворюється на звичайний текст ASCII
    ' i навпаки, в тексті UTF-8 будь-який байт із значенням менше, ніж 128 зображає символ ASCII з тим же кодом'''
    ord('a') , '#97' 'Чтоб узнать код символа'
    chr(97), 'a' 'Чтоб узнать символ по коду'
    def ASCII(): # Переобразование в ASII КОД и ОБРАТНО
        test = ' '.join(str(ord(el)) for el in s)
        new = test.split(' ')
        check = []
        for el in new:
            check.append(int(el))
        print(check)
        ind = ''.join(chr(char)for char in check)
        print(ind)

    def UTF_8(): # Переобразования в UTF-8       
        s = "Привіт!"
        utf8 = s.encode()
        print(f"UTF-8: {utf8}")

        utf16 = s.encode("utf-16")
        print(f"UTF-16: {utf16}")

        cp1251 = s.encode("cp1251")
        print(f"CP-1251: {cp1251}")


    def HEX(): # Переобразарование в HEX
        s = 'Hello world'
        test = ' '.join(str(ord(el)) for el in s)
        new = test.split(' ')
        check = []
        for el in new:
            check.append(int(el))
        for num in check:
            print(hex(num))

def Masiw_Bytes(): #Масив Байтов
    byte_array = bytearray(b'Kill Bill!')
    byte_array[0] = ord('M'), 'Изменения значений '
    byte_array.append(ord('!')), 'Добавление значений'
    string = byte_array.decode('UTF-8'), 'Изменяем bytearray на string'

def Archiv():
    pass

def parametrs_file():
    '''Параметри:
file - шлях до файлу у вигляді рядка. Це може бути повний шлях або шлях відносно поточного каталогу виконання.
mode (необов'язковий) - режим, в якому буде відкрито файл. Ось основні режими які ми будемо використовувати:
'r' - читання (за замовчуванням). Файл має існувати.
'w' - запис. Створює новий файл або перезаписує, що вже існує.
'a' - додавання. Дописує в кінець файлу, не перезаписуючи його.
'b' - бінарний режим (може бути використаний разом з іншими, наприклад 'rb' або 'wb').
'+' - оновлення (читання та запис).
buffering (необов'язковий) - визначає буферизацію: 0 для вимкненої, 1 для включеної буферизації рядків, більше 1 для вказання розміру буфера у байтах.
encoding (необов'язковий) - ім'я кодування, яке буде використовуватися для кодування або декодування файлу.
errors (необов'язковий) - вказує, як обробляти помилки кодування.
newline (необов'язковий) - контролює, як обробляються нові рядки.
closefd (необов'язковий) - має бути True (за замовчуванням); якщо вказано False, файловий дескриптор не буде закритий.
opener (необов'язковий) - визначає спеціальну функцію для відкриття файлу.

Біт (скорочено від "binary digit" або "двійкова цифра") є основною одиницею інформації в обчислювальній техніці та цифровій комунікації.
Біт може мати одне з двох значень: 0 або 1. Ви можете думати про біт, як про відповідь на просте питання: "так/ні" або "вимкнено/увімкнено".

Байт - це послідовність з 8 бітів, яка є стандартною одиницею вимірювання кількості інформації в комп'ютерах. 
Один байт може представляти 256 різних станів. Від 00000000 до 11111111 у двійковому форматі або від 0 до 255
десятеричному, що дозволяє кодувати широкий спектр інформації, наприклад, символи тексту, частини зображень або звуку.

У комп'ютерах кожен символ у тексті (наприклад, літера або цифра) зазвичай кодується одним байтом.
Наприклад, у кодуванні ASCII символ 'A' представляється як 01000001. Усі дані на комп'ютері зберігаються у вигляді байтів. 
Наприклад, текстовий файл розміром у 1 кілобайт займає 1024 байти в пам'яті комп'ютера. Коли дані передаються через інтернет мережу, вони також розбиваються на байти.'''
