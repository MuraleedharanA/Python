import pandas as pd
import re
"""Create a python program to read a csv file and get the freq of all words in the file and show it as DF"""

novel = open(r"C:\Users\Administrator\Desktop\UST_Training\Milestones\Novel.csv")

word_dict={}
content=novel.read()
#find all words in the novel
allWords=re.findall(r"\b[A-Za-z]+\b",content)   
for word in allWords:
        if(not word in word_dict):
            #add word to dic and find all occurance using regex
            word_dict[word] = len(re.findall(word,content)) 


dataframe_words=pd.DataFrame(list(word_dict.items()),columns=['Word','Count'])
dataframe_words.to_csv("WordCount.csv")
