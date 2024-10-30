import re

pattern='\d+'
string=input('Input your String :')

result=re.findall(pattern,string)
print(result)