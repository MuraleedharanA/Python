count=1
while(True):
    print("hi")
    if(random.choice(range(10000))):
        print("finally!!!")
        count+=1
        break
print(count)
