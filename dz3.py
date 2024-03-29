# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

'''первый метод - более быстрый'''
# A = []
# list_len = int(input("Введите количество элементов в массиве: "))
# for _ in range(list_len):
#     A.append(int(input(f"Введите число: ")))
# print(A)

# input_x = int(input('Введите число X: '))

# count_x = A.count(input_x)
# print("Число", input_x, "встречается в массиве", count_x, "раз(а)")



'''второй метод'''
# A = []
# list_len = int(input("Введите количество элементов в массиве: "))
# for _ in range(list_len):
#     A.append(int(input(f"Введите число: ")))
# print(A)

# input_x = int(input('Введите число X: '))

# count_x = 0
# for i in A:
#     if i == input_x:
#         count_x += 1

# print("Число", input_x, "встречается в массиве", count_x, "раз(а)")


# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

# A = []
# list_len = int(input("Введите количество элементов в массиве: "))
# for _ in range(list_len):
#     A.append(int(input(f"Введите число: ")))
# print(A)

# input_x = int(input('Введите число X: '))

# min_diff = float('inf')
# closest = A[0]
# for i in A:
#     diff = abs(i - input_x)
#     if diff < min_diff:
#         min_diff = diff
#         closest = i
# print ("Ближайший элемент в массиве A к числу", input_x, "равен", closest)


# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.
# Ввод:
# ноутбук
# Вывод:
# 12

values = {'а': 1,'в': 1,'е': 1,'и': 1,'н': 1,'о': 1,'р': 1,'с': 1,'т': 1, 'д': 2,'к': 2,'л': 2,'м': 2,'п': 2,'у': 2, 'б': 3,'г': 3,'ё': 3,'ь': 3,'я': 3, 'й': 4,'ы': 4, 'ж': 5,'з': 5,'х': 5,'ц': 5,'ч': 5, 'ш': 8,'э': 8,'ю': 8, 'ф': 10,'щ': 10,'ъ': 10,
          'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1, 'l': 1, 'n': 1, 's': 1, 't': 1, 'r': 1, 'd': 2 ,'g': 2, 'b': 3, 'c': 3, 'm': 3, 'p': 3, 'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4, 'k': 5, 'j': 8, 'x': 8, 'q': 10, 'z': 10}
word = input("Введите слово: ")
score = 0
for letter in word:
    score += values[letter]
print( "Стоимость слова", word, "равна", score)
