import re

str = r'^[a-zA-Z0-9_-]{0,4}(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]{0,4}$'
if re.match(str,'helxdl.abc@163.com'):
    print('ok')
else:
    print('notok')
if re.match(str,'h.abasdwac@163.dcom'):
    print('ok')

m = re.match(r'\d{3}\-\d{3,8}', '010-12345')
# print(dir(m))
print(m.string)
print(m.pos, m.endpos)

# 分组
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.groups())
print(m.group(0))
print(m.group(1))
print(m.group(2))

# 分割
p = re.compile(r'\d+')
print(type(p))
print(p.split('one1two3three3four4'))
print(m.group(2))

t = '20:15:45'
re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.groups())
