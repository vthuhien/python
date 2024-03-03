import os
# print(os.getcwd())

# os.chdir(r'C:\Users\Admin\Desktop\python\test')
 
# f = open('test.txt','w')
# f.close()

# os.rename('test.txt','thuhien.txt')

# os.remove('thuhien.txt')

# from shutil import copyfile
# copyfile('test.txt','thuhien.txt')

# f=open('test.txt','a')
# f.write('thuhiencutis1tg'+'\n')
# f.close()

# f = open('thuhien.txt',mode='a',encoding='utf-8')
# f.write('vũ thị thu hiền'+'\n')
# f.close()

f=open('thuhien.txt',mode='r',encoding='utf-8')
list_line = f.readlines()
print(list_line)

f=open('test.txt',mode='r')
list_line = f.readlines()
print(list_line)
f.readlines()