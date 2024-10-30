import re
pattern='^a....s$'
stringTest='aqqqqs'

result=re.match(pattern,stringTest)

if result:
    print("match found")
else:
    print("no match")
