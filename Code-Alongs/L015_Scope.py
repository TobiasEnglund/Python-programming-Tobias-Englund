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
