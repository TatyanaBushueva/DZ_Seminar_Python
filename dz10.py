import random, pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
# lst += ['somebody'] * 5 # Алгоритм работает не только с двумя видами значений
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
# print(data)
# print(data.head(n=5)) 

fields = list(set(data['whoAmI'])) # Определяем список с уникальными полями через множество
OneHotDict = dict.fromkeys(fields) # Делаем заготовку словаря
for k in OneHotDict: 
    OneHotDict[k] = []  
# print(OneHotDict) # Пока что пустой словарь
# Распределяем элементы данных в записи словаря
for i in range(0,len(data['whoAmI'])):
    for j in range(0,len(fields)):
        if data['whoAmI'][i] == fields[j]:
            OneHotDict[fields[j]].append(True)
        else:
            OneHotDict[fields[j]].append(False)
# Формируем набор данных из словаря с добавленными в поля необходимой строки whoAmI_
res_get_dummies_my = pd.DataFrame({'whoAmI_' + k: v for (k,v) in OneHotDict.items()})
print('One Hot by my_get_dummies')
print(res_get_dummies_my.head(n=5)) # Выводим только голову из пяти значений
#-----------------------------------------------------------
#Сравниваем со стандартной функцией
res_get_dummies = pd.get_dummies(data, columns = ['whoAmI'])
print('One Hot by pandas_get_dummies')
print(res_get_dummies.head(n=5))



# print(res_get_dummies.keys())


# print(OneHotDict)
# OneHotDict[fields[0]] = [i for i in range(len(data['whoAmI']))]
# OneHotDict[fields[1]] = [i for i in range(len(data['whoAmI']))]
# print(OneHotDict.keys())
# for i in OneHotDict:
#     s = 'whoAmI_'+ i
#     OneHotDict[s] = OneHotDict.pop(i)
#     print(s)
# OneHotDict['whoAmI_'] = OneHotDict.pop('robot')
# print(OneHotDict)
# dict1_keys = {k*2:v for (k,v) in dict1.items()}

# print({'whoAmI_' + k: v for (k,v) in OneHotDict.items()})
# print(OneHotDict)