"""
split the file content
check condition
"""

file_handler = open(r"sample.csv")
for line in file_handler:
    l=line[:-1:]
    value_list=l.split(',')
    print(value_list[1])
    if(value_list[1]=='test'):
        print(l)
