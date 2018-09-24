#Functions Basic II 
#2018 09 14
#Cheung Anthony

# 1. Countdown - Create a function that accepts a number as an input.  Return a new array that counts down by one, from the number (as arrays 'zero'th element) down to 0 (as the last element). 
# For example countDown(5) should return [5,4,3,2,1,0].
# def Countdown(num):
#     li=[]
#     for i in range(1,num,-1):
#         li.append(i)
#     return(li)
# print(Countdown(5))

# def Countdown(a):
#     li=[]
#     for i in range(a,-1,-1):
#         li.append(i)
#     return(li)
# print(Countdown(5))

# 2. Print and Return - Your function will receive an array with two numbers. 
# Print the first value, and return the second.

# def printreturn(tisl=[]):
#     x=len(tisl)
#     print(tisl[0])
#     return(tisl[x])
# arr=[1,2,3]
# print(printreturn(arr))

# 3. First Plus Length - Given an array, return the sum of the first value in the array, plus the array's length.

# def firstpluslength(tisl):
#     y=len(tisl)
#     first=tisl[0]
#     return(y + first)
# arr2=[1,2,3,4]
# print(firstpluslength(arr2))

# 4. Values Greater than Second - Write a function that accepts any array, and returns a new array with the array values that are greater than its 2nd value.  Print how many values this is.  If #the array is only one element long, have the function return False

# def greater2nd(tisl,value):
#     cnt=0
#     for i in range(len(tisl)):
#         if tisl[i] > value:
#             cnt=cnt+1
#     return(cnt)
# arr3=[4,2,3]
# print(greater2nd(arr3,2))
               

def greater2nd(tisl,value):
    if len(tisl)==1:
        return("False")
    else:
        cnt=0
        new=[]
        for i in range(len(tisl)):
            if tisl[i] > 2:
                cnt=cnt+1
                new.append(tisl[i])
    return(new,cnt)
arr3=[4,2,3]
print(greater2nd(arr3,2))

# 5. This Length, That Value - Write a function called lengthAndValue which accepts two parameters, size and value. 
# This function should take two numbers and return a list of length size containing only the number in value. For example, lengthAndValue(4,7) should return [7,7,7,7]

# def lengthvalue(l,v):
#     out=[]
#     for i in range(l):
#         out.append(v)
#     return(out)
# print(lengthvalue(4,7))

