#python modify strings

#upper case : 
a = "hello world"
print(a.upper())

#lower
print(a.lower())


#strip() function
b = "    Hello   ,  World!        "
print(b.strip()) # returns "Hello, World!"
b = b.strip()
print(b + "hello")


#replace() function  : The replace() method replaces a string with another string:
a = "Hello , setu , world" 
print(a.replace("H" , "J")) ; 
print(a.replace("Hello" , "zakur"))
print(a.replace("hello" , "zakur")) # since the given "hello" string is not matching so it will not make any changes in the string and will print the original string only.


# split string:
#The split() method returns a list where the text between the specified separator becomes the list items.
a = "a lazy cow jumps over the lazy , , cow ;"
print(a.split(",")) ; 


a = "a lazy cow jumps cow over tcow he lazcowy , , cow ;"
a = "mangoXapplexTHE AAM"
print(a.split("X")) ; 
print(a.split("p")) ; 

i = 0 ; 
for x in a.split("p"):
    print(x) 
    i = i+1
print(i)

