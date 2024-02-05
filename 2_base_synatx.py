#   Библиотеки 
import time
import random
import typing

#   Основные типи и структуры //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

types = [
    None, # Значение ничего
    True,False, bool,
    1,  int, # Целое число
    5 + 1j, complex, # 5-Pеальное часть, 1-Воображаемая часть, j-Символ воображаемой единицы
    1.1,  float, # Число с плавающей запятой
    ' ', " ", """ """, f'', r'', str, #
    b'',  bytes, # Байт
    [], list, # Список 
    (),  tuple, # Кортеж
    {1, },  set, # Множество
    { },  dict # Словарь
    ]

# Основные операторы /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

_ = 1 + 2
_ = 1 - 2
_ = 1 * 2
_ = 1 ** 2
_ = 1 / 2
_ = 1 // 2
_ = 1 % 2 
_ = 1 and 2
_ = 1 or 2
_ = 1 > 2
_ = 1 >= 2
_ = 1 < 2
_ = 1 <= 2

# Тернарный оператор /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

python = True
name = 'Serhii' if python else 'No name'

python = None
name = python or 'Python', ' Быстрая проверка переменной'

# Оператор Match //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

fruits = ('banana', 'orange') , 'Поиск подходящего шаблона, если нету выполняеться заглушка'
match fruits: 
    case 'banana', 'orange':
        print(f'Banana')
    case _:
        pass

pets = ['cat', 'dog', 'fish']
match pets:
    case[_,_,'fish']:
        print(f'DOG,CAT,FISH')


#Цикл For /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
for _ in range('start','stop','step'):
    break 
else:
    pass

some_list = ["apple", "banana", "cherry"] , 'Перебор списка индекс значение'
for index, value in enumerate(some_list):
    print(index, value)

list1 = ["зелене", "стигла", "червоний"] , 'Перебор 2 и более списков'
list2 = ["яблуко", "вишня", "томат"]
for number, letter in zip(list1, list2):
    print(number, letter)


#   Comprehensions ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

a = [i for i in types]
b = (i for i in types)
c = {i for i in types if isinstance(i, typing.Hashable)}
d = {str(i): i for i in types}

#   Присваивание, распаковка, срезы /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

e, *f, g = types
h = [*f]
_ = [1, 2, 3][:]

_ = {**{}} ,   'Распаковка Словаря в другой словарь '

#   Утверждение assert  /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

assert h, 'test'


#   Цикл While ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

while a:
    a.pop()

while a:
    break
else:
    pass

#   Функции ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'Изменямые возвращение','Int','Str','Float','Tuple'
'Не Изменямые возврашение','List','Dict','Set'
def name (name:str = 'Serhii', age:int=24)-> tuple:
    return name, age

'*args' 'Принимает любое количество параметров в функцию и делает из них кортеж/////////  *args////////'
def main(*args)->str: 
    pass
print(main('hello', ' ', '', 'world','!'))
'**kwargs' 'Принимает любое количество параметров в функцию и делает из них словарь/////////  **kwargs////////'
def prest(**kwargs):
    for key, values in kwargs.items():
        print(f'Key: {key}, Values: {values}')
prest(person_1 = 'Serhii', age_person_1 = 24, person_2 = 'Karina',age_person_2 = 22)

def func (text: str, space: str, action: typing.Callable) -> None:
    if not text:
        return
    
    print(space + action(text))
    func(text[1:], space + ' ', action)
    print(space + action(text))

#   Lambda функции ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
func('*' * 11, '', lambda text: ' '.join(i for i in text))

#   Декораторы  ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def decorator(multiplier: int):

    def dec(func: typing.Callable):
        #Области видимости функции
        global a, b, c, d
        nonlocal multiplier

        if multiplier % 2 == 0:
            multiplier += 1
        
        def wrap(*args, **kwargs):
            for _ in range(multiplier):

                #Генераторы
                yield func(*args, **kwargs)
        return wrap
    return dec

@decorator(10)
def f(num: int)-> int: 
    return num 

qwe = [*f(1)]
print(qwe)

#   Условия  ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
if i := d.get(''):
    pass
elif not (q := d.get(1)):
    pass
else:
    ...

#   Исключения и их обработка  ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
SyntaxError, 'синтаксична помилка.'
IndentationError, 'помилка, яка виникає, якщо у виділенні блоків інструкцій пробілами допущена помилка.'
TabError, 'виникає, якщо в одному файлі використовувати пробіли i табуляції для виділення блоків інструкцій.'
TypeError, 'виникає, коли операція зі змінною цього типу неможлива.'
ValueError, 'виникає, коли тип операнда відповідний, але значення таке, що операцію неможливо виконати.'
ZeroDivisionError,  'ділення на нуль.'
try:
    1/0
except ZeroDivisionError as exc:
    pass
else:
    pass
finally:
    ...

#   Классы ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class A:

    class_attrs = None

    def __init__(self, *args, **kwargs):
        self.args, self.kwargs = args, kwargs
        self.__test.arg = None

    def main(self) -> None:
        ...

    #2 usages
    @property
    def test_arg(self) -> typing.Any:
        return self.__test_arg
    
    #1 usage
    @test_arg.setter
    def test_arg(self, value: typing.Any):
        self.__test.arg = value

class B(A):

    def main(self) -> None:
        super().main()
        print(self.test_arg)

    @classmethod
    def create(cls, *args, **kwargs) -> 'B':
        return cls(*args, **kwargs)
    
    @staticmethod
    def get_test() -> str:
        return 'test'
      