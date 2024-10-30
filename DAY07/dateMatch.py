import re

pattern=r'\b\d{4}[-/]\d{2}[-/]\d{2}'
inputString='sample 2013-04-02 sheet shared 2024/12/23 with HOD'

result=re.findall(pattern,inputString,re.IGNORECASE)
print(result)