#   Кортежы Tuple ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

my_tuple = (1, 2), 'Создание Tuple'
my_tuple = tuple([1, 2])
my_tuple = my_tuple[:] , 'Срезы' / 'Вывод всего'
my_tuple = tuple(set(my_tuple)) , 'Удаление повторяющихся елементов. Кортеж -> Множество -> Кортеж'