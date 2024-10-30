def removeVowels(input):
    """Function to remove vowels from string"""
    vowels=["a","e","i","o","u"]
    outval=""
    for i in range(len(input)):
        if(not input[i] in vowels):
            outval=outval+input[i]
    return outval
print("Input a string with vowels :")
input=input()
print("String after removing Vowels : ",removeVowels(input))


