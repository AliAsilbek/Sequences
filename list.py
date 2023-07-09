# str
letters = 'Hello world!'
print(len(letters))
print(letters[2])
print(letters[3:8])
# list неизменяемый []
# упорядоченные изменяемые коллекции объектов произвольных типов

job = ['max', 'kile', 'rey']
friends = ['mishel', 'dick']
print(type(job))  # имеет тип list
job.extend(friends)  # 1 в список job присоединяются дублируются данные с списка friends
print(job)
job.insert(1, 'Joseph')  # 2 тоже самое что и append, но вместо добавления, заменяет первый элемент списка
job.remove('mishel')  # 3 убират из списка mishel
job.append('roy')  # 4 добавляет roy в список
job[1] = 23  # данные списка возможно изменять
print(job)  # c joseph
print(job.pop(1))  # 5 убирает из списка 1 элемент списка и выводит его на экран
print(job)  # без joseph
print(job.sort())
job.append(friends)
job[3] = "karlson" # прибавление по индексу
print(job)
del job[3] # удаление по индексу
print(job)

# tuple неизменяемый - кортежи ()
letters = tuple('hello world')
print(letters)
office = ('kate', 'Michael')
job = ('max', 'kile', 'rey', 'max', 'max', 'max', 'max')
print(type(job))  # имеет тип tuple - кортеж
# job.remove('max') # в данном случае произойдет ошибка, потому что кортеж не возмонжо изменять. Тоже самое будет и c append, extend, pop insert и т.д.
print(job.index('max'))  # 1 показывает индекс элемента
print(job.count('max'))  # 2 показывает количество max в кортеже job

print(job)

# dictionary изменяемый {'key':"value",...}
# неупорядоченные коллекции произвольных объектов с доступом по ключу

job = {
    'manager': "Lucy",
    'waiter': "Michael",
    'salesman': "Ibn - Al Rashid"
}
print(job)
print(job.keys())  # 1. Выводит ключи словаря
print(job.values())  # 2. выводит значения словаря
print(job.items())  # 3. выводит ключ-значение словаря
print(job.pop('manager'))  # 4. убирает из списка 1 элемент списка и выводит его на экран
print(job.get('salesman'))  # 5. возвращает значение ключа

# set изменяемый {}, set()
# приемущества: 1. "контейнер", содержащий не повторяющиеся элементы в случайном порядке.
# Множества удобно использовать для удаления повторяющихся элементов

job = {'ali', 'ali', 'ali', 'artyom', 'kanat'}
office = {'Aibek', 'ali'}
print(job)
print(len(job))  # 1. пишет длину множества
print(job.isdisjoint(office))  # 2. проверяет множество office на его вхождение в множество job. Если хотя бы один элемент входит, выводит False
print(job.union(office))  # 3. объеденяет множества office и job
print(job | office)  # объеденяет множества office и job
print(job - office)  # 4. удаляет из job все элементы которые есть в office
print(job & office)  # 5. объеденяет элементы множеств job и office
