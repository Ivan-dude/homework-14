# 1.Функция с параметрами по умолчанию:
def print_params(a=1, b='строка', c=True):
    print(a, b, c)
print_params()
print_params('целое предложение', False, 24)
print_params(23,33)
print_params(b=25)
print_params(c=[1,2,3])
print_params(www:=1111,2, 3) #ещё один вариант, изменить параметр 'a'
#print_params(1,2,3,4) #задано большее кол-во арг., чем в определении функции

# 2.Распаковка параметров:
value_list = [25, True, 'Строка']
value_dict = {'a':25, 'b':True, 'c':'Строка'}
print_params(*value_list)
print_params(**value_dict)

#3.Распаковка + отдельные параметры:
value_list2 = [25, True]
print_params(*value_list2, 42)