a=input("Enter a number\n")

count=0 #counts the zeroes of number
rem=0 #remainder of input
zero=0
l=0
l=len(a)
for i in a: #traversing through a as a string
    a=int(a) #converting a to number so we can do maths on it
    if(a%10==0): #if the remainder of a is equal to zero
        zero=l-1 #reduce lenght by 1
print(zero) #print of end result
