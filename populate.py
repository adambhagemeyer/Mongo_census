import os
import alter_collections as add
import Socioeconomic
import pymongo


n = 1
content_list = ''
with open('./counties.txt') as f:
    content_list = f.readlines()[n:]
# print('=============================================================')
# print('=============== File Loaded - Populating... =================')
# print('=============================================================')
# print('=============== This is gonna take a while ==================')
# print('=============================================================')
# x = n
# for l in content_list:
#     y = l.split()
#     add.addToDB(y[1])
#     os.system('clear')
#     print(f'{x}/3220 Files Added...')
#     if x != 0:
#         prog = round(x / 3220, 2)
#         print(f'Progress: {prog}%')
#         print('\n')
#         print('\n')
#     x+=1


# print('=============================================================')
# print('=============================================================')
# print('===================== Load Completed! =======================')
# print('=============================================================')
# print('=============================================================')
x = n
for l in content_list:
    y = l.split()
    Socioeconomic.addInfo(y[1])
    os.system('clear')
    if x != 0:
        prog = round(x / 3220, 2)
        print(f'Progress: {prog}%')
        print('\n')
        print('\n')
    x+=1

# x = []
# for l in content_list:
#     y = l.split()
#     if add.checkDB(y[1]) == {}:
#         x.append(y[1])
#         print(f"{y[1]}: Doesn't exist")
#         print('\n')
#     else:
#         print(f"{y[1]}: Does exist")
#         print('\n')

# print('\n')
# print('\n')
# print('\n')
# print('\n')
# print('Data not added because of issues with the API: ')
# print(x)
