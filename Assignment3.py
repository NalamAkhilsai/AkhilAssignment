#Reading a file and printing without spaces after each line
# f = open('newfile','r')
# print(f.read())

#Reading a file
# f = open('newfile','r')
# for i in f:
#     print(i)

#writing in a file
# f = open('newfile','a')
# f.write("thanks\n")
# f.close()

#to strip spaces
# file = open('newfile','r')
# for i in file:
#     rem = i.strip()
#     print(rem)

#to split the string based on delimitter
# with open('student.dat','r') as file:
#      for i in file:
#          rem = i.split(';')
#          print(rem)

#to print id and name
# with open('student.dat','r') as file:
#      for i in file:
#          rem  = i.split(';')
#          print(rem[1],rem[5])


#To print student_semi.dat
# import os
#
# file = 'student_semi.dat.txt'
# if os.path.exists((file)):
#    with open(file) as student_file:
#        for i in student_file:
#            eachline = i.strip()
#            line = eachline.split(';')
#            print(line)

#To print student_comma.dat
# import os
#
# if os.path.exists(('student_comma.dat.txt')):
#     with open('student_comma.dat.txt') as file:
#         for i in file:
#             i = i.strip()
#             i = i.split(',')
#             print(i)
#     #print(file.read())


#To print data from student_double_semi.dat.txt
# import os
# if os.path.exists('student_double_semi.dat.txt'):
#     with open('student_double_semi.dat.txt') as file:
#         for i in file:
#             i = i.strip()
#             i = i.split(';;')
#             print(i)

#converting epoch time to normal time
# import os
# import datetime
#
# if os.path.exists('student.dat'):
#     mod_time = os.path.getmtime('student.dat')
#     normal_time = datetime.datetime.fromtimestamp(mod_time)
#     print(mod_time,normal_time)

# To print filesize
# import os
# if os.path.exists('student.dat'):
#     filesize = os.path.getsize('student.dat')
#     print(filesize)

# #to find the number of characters present in a file
# import os
# file = 'student.dat'
# if os.path.exists(file):
#     with open(file) as file:
#         i = len(file.read())
#         print(i)

# To find the numbers of line present in a file
import os
file = 'student.dat'
if os.path.exists(file):
    with open(file) as file:
        i = len(file.readlines())
        print(i)

#To find file name
import os
filename = 'C:\Users\Nalam.Sai\PycharmProjects\pythonProject\student_semi.dat.txt'
name = os.path.basename(__file__)
print(name)

