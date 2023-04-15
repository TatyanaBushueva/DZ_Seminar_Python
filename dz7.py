# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) 
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, 
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу 
# с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не 
# в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам 


# sentence = input('Введите строку: ')

# def count_vowels(word):
#     vowels = 'уеыаоэию'
#     count = 0
#     for letter in word: 
#         if letter in vowels: 
#             count += 1
#     return count

# words = sentence.split()
# # for word in words: 
# #     print(count_vowels(word))
    
# all_is_equal = True
# last_count = count_vowels(words[0])

# for i in range(1, len(words)):
#     if last_count != count_vowels(words[i]):
#         all_is_equal = False

# if all_is_equal:
#     print('Парам пам-пам')
# else:
#     print('Пам парам')



# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, 
# у операции умножения.

# *Пример:*

# **Ввод:** `print_operation_table(lambda x, y: x * y) ` 
# **Вывод:**
# 1 2 3 4 5 6

# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

def print_operation_table(oper: callable,
                          num_colums: int = 6,
                          num_rows: int = 6) -> None:
    table = [list(range(i, i + num_colums)) for i in range(1, num_rows + 1)]
    for i in range(1, len(table)):
        for j in range(1, len(table[i])):
            table[i][j] = oper(table[i][0], table[0][j])
    show_table(table)

 
def show_table(table: list[list[int]]) -> None:
    print('\n'.join('\t'.join(map(str, row)) for row in table))



oper = lambda x, y: x * y
n = 4
m = 6
print_operation_table(oper, n, m)
