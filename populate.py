import os
import alter_collections as add



content_list = ''
with open('./counties.txt') as f:
    content_list = f.readlines()[1:]
print('=============================================================')
print('=============== File Loaded - Populating... =================')
print('=============================================================')
print('=============== This is gonna take a while ==================')
print('=============================================================')
x = 0
for l in content_list:
    y = l.split()
    add.addToDB(y[1])
    os.system('clear')
    print(f'{x}/3220 Files Added...')
    if x != 0:
        prog = round(x / 3220, 2)
        print(f'Progress: {prog}%')
        print('\n')
        print('\n')
    x+=1


print('=============================================================')
print('=============================================================')
print('===================== Load Completed! =======================')
print('=============================================================')
print('=============================================================')

    
