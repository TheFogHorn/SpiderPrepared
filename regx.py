import re

str = r'^[a-zA-Z0-9_-]{0,4}(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]{0,4}$'
if re.match(str,'helxdl.abc@163.com'):
    print('ok')
else:
    print('notok')
if re.match(str,'h.abasdwac@163.dcom'):
    print('ok')
