#To print largest,smallest,2nd largest number
# num = [2,5,1,8,3]
# largest = max(num)
# smallest = min(num)
# num.sort(reverse=True)
# secondlargest = num[1]
# print("largest number is :",largest)
# print("smallest number is :",smallest)
# print(secondlargest)

#To remove 3rd ,7th,4th element from list
# list1 = [1, 4, 10, 30, 60, 70, 80 , 100]
# list2 = [3,7,4]
# list2.sort(reverse=True)
# for i in list2:
#     list1.pop(i)
# print(list1)

# Reversing a string and printing if vowel count is greater than 2
# string1 = "python training"
# list1 = ['a','e','i','o','u']
# def rev_string(string1):
#     ret = string1[::-1]
#     return ret
# reversed = rev_string(string1)
# def counting_vowels(reversed):
#     count = 0
#     for i in string1:
#         if i in list1:
#             count = count + 1
#     return count
# vowellist = counting_vowels(reversed)
# if vowellist > 2:
#      print("true")
# else:
#     print("false")


# To delete the second occurrence of 1 from the list
a = [1,2,1,1,4,5]
b = len(a)
i = 1
count = 0
for j in range(b):
    if a[j] == i:
        count = count+1
        if count == 2:
            del a[j]
            break
print(a)


