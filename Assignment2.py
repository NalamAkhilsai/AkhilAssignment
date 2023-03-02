#numbers which are divisible by 7
# list1 = [21,7,9,11,14,15,20]
# list2 = []
# def div_by_7():
#    for i in list1:
#        if i%7 == 0:
#           list2.append(i)
#    return list2
# dividednum = div_by_7()
# print(dividednum)
from itertools import count

#Change odd characters to uppercase and even to lowercase in a string.
# name = 'akhil'
# changed_name = ''
# length1 = len(name)
# def even_odd():
#     global changed_name
#     for i in range(length1):
#         if i % 2 == 0:
#             changed_name = changed_name + name[i].lowe()
#         else:
#             changed_name = changed_name + name[i].upper()
#     return changed_name
# after_change = even_odd()
# print(after_change)



#prog to print prime num from the list
# my_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# for num in my_list:
#     #prime = False
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 #prime = True
#                 break
#     # if prime == False:
#     #    print(num)
#         else:
#             print(num)


#To count no of words in a string
statement = 'There are so many people are working everything is good'
word = len(statement.split())
print(word)


