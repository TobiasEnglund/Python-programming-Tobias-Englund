# In python we have 2 types of scope (life-time of a variable)
# Local scope: Only available locally in a function.
# Global scope: Availabe through execution of program.

name = "Fredrik"

def main():
    global name
    name = "Kalle"
    print(name)

print(name)
main()
print(name)

# Python doesn't have block scope, but this is used in most other languages, such as c#, c++, java
# if name == "Fredrik":
#     last_name = "Johansson"
    
# print(last_name)

# for i in range(3):
#     print(i)

# print(f"i = {i}")

# In Python we have two types of scope (life-time of a variable)
# Local scope: Only available locally in a fuunction
# Global scope: Available through execution of the program

name = "Tobias"

def main():
    global name             # Change the scope of the the variable "name" to global
    name = "Daniel"
    print(name)
   
print(name) 
main()
print(name) 

# Python doesn't have block scope like some other language (Java, c#, c++, etc)
# if name == "Tobias":
#     last_name = "Englund"
    
# print(last_name)

# for i in range(10):
#     print(i)
