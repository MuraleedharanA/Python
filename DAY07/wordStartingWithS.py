import re

pattern=r'\bs\w*'
inputString='sample sheet shared with HOD'

result=re.findall(pattern,inputString,re.IGNORECASE)
print(result)