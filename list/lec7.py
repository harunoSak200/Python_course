#change list items:

lis1 = ["apple" , "banana" , "cherry"]
print(lis1)
lis1[1] = "litchi"
print(lis1)

#change a range of item values:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrent" , "drangonfruit"]
print(thislist)


"""
If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

"""
thislist[1:2] = ["litchi" , "jackfruit"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["watermelon"]
print(thislist)


#insert items : 
lis1 = ["apple" , "banana" , "cherry"]
lis1.insert(-7 , "lemons")
print(lis1)