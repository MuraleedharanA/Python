##get max key in the given dictionary
maxkey=-1
dictionary_sample={1:3,2:3,4:5,6:7,45:4}
for key in dictionary_sample:
    if(maxkey<key):
        maxkey=key
print("MaxKey",maxkey)
print("MaxKey",max(dictionary_sample.keys()))