#python format strings



#we can only add strings into the strings
# age = 36
# txt = "My name is John, I am " + age   # illegal cannot add the strings into the number.
# print(txt)

# F-strings

"""
F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.

"""

age = 36 
txt = f"my son of the {age}"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 59
txt = f"The price is {(price-5)*10:.2f} dollars"
print(txt)


