

 #1////////////////////////

text = input("enter your char : ")

vowels = ['a', 'e', 'i', 'o', 'u']

count = 0
for char in text:
    if char in vowels:
        count += 1

print("numbers of characters :", count)

 #2////////////////////////


names = ["Mohamed", "Ahmed", "Ali"]
names.sort()
print(names)
names.reverse()
print(names)
 #3////////////////////////


l2 = "welcome to iti iti is very professional"
print(len(l2))
print(l2.count("iti"))


 #4////////////////////////
word = "education"
vowels = ['a', 'e', 'i', 'o', 'u']

result = ""  

for char in word:     
    if char not in vowels: 
        result += char    

print(result)  


# #5/////////////////////////
# myChar = "i"
# myStr = input("Enter a string: ")

# for index in range(len(myStr)):
#     if myStr[index] == myChar:
#         print("The location of i is:", index)

# #7///////////
# myNum = int(input("Enter a number: "))
# for i in range(1, myNum + 1):
#         print('+' * (myNum - i) )
        
print('='*5)




 
 
