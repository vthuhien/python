# demo1
import re
regexl = re.compile("vthuhien (.*?) lum")
chuoi = "vthuhien cuti lum"
kq = regexl.search(chuoi)
# hoặc sử dung findAll, sử dụng khi có nhiều regex object quá
finish = kq.groups(1)
print(finish)

# demo2
regex = re.compile('(.*?) cuti lum')
noidung = '''thuhien cuti lum
meo cuti lum'''
test = regex.findall(noidung)
print(test)