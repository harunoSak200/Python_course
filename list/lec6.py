#basic list representation
lis1 = [1 , "hello" , True , "sdfs"] 
print(lis1)

#list length :
print(len(lis1))

#The list() constructor : 
#It is also possible to use the list() constructor when creating a new list.

thislist = list(("apple" , 1 , True))
print(type(thislist))


lis1 = ["apple" , "mango" , "banana" , "grapes" , "litchi" , "guava"]

#access items:
print(lis1[1])


#range of the indexes : 
print(lis1[0:])   # or lis1[:] is the same.
print(lis1[:])
print(lis1[0:5])
print(lis1[2:])
print(lis1[1:1])
print(lis1[:1])
print(lis1[2:5])


#negative indexing:
print(lis1[-1])
print(lis1[-5:-2])

print(lis1[1:-1])









