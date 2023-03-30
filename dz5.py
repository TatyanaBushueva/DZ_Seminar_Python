# 3*. Sample Input
# ["eat", "tea", "tan", "ate", "nat", “bat"]
# Sample Output
# [ ["ate", "eat", "tea"], ["nat", "tan"], ["bat"] ]
# Т.е.сгруппировать слова по "общим буквам".



def group_letter(input_list):
    word_dict = {}
    for word in input_list:
        if (frozenset(word), len(word)) not in word_dict:
            word_dict[(frozenset(word), len(word))] = [word]
        else:
            word_dict[(frozenset(word), len(word))].append(word)
    res_list = []

    for value in word_dict.values():
        res_list.append(value)
    return res_list

print(group_letter(["eat", "tea", "tan", "ate", "nat", "bat"]))





# 6. Дана строка ( возможно, пустая), состоящая из букв A-Z:
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида:
# A4B3C2XYZD4E3F3A6B28 И сгенерирует ошибк,
# если на вход пришла невалидная строк.
# Пояснения: Если символ встречается 1 раз, он остается
# без изменений;
# Если символ повторяется более 1 раза, к нему добавляется
# количество повторений.
# import pickle

# def RLE(string):
#     out = ""
#     count = 1
#     if len(string) == 0:
#         return ""
    
#     for i in range(1,len(string)):
#         if string[i] == string[i-1]:
#             count +=1
#         else:
#             if count == 1:
#                 out += string[i-1]
#             else:
#                 out += string[i-1] + str(count)
#                 count = 1
#     if count == 1:
#         out += string[-1] 
#     else:
#         out += string[-1] + str(count)
#     return out

# inp = input("Введите строку: ")
# if all(c.isalpha() and c.isupper() and c.isascii() for c in inp):
#     print(RLE(inp))
# else:
#     print("Введена невалидная строка")










