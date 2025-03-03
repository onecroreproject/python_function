
# Function......

''' Function is a block of code only runs when the function calls.
    Can pass parameter in the function.
    Function is defined using "def" keywords. '''

# Create the function

def fun(): 
    pass

# Call the function

def fun():
    print("Function")
fun()                 # function calling


def Ram(self):
    return "ram bad"
   
Ram()


#Arguments.......
''' Can pass the arguments in the function inside the parenthesis. '''
def fun(fruit, color):
    print( f"{fruit}, {color}")
fun( "cherry", "red")
fun("Muskmelon", "yellow")

# Arbitrary Arguments.....

'''  arguments that allow a function to accept an unlimited number of arguments. 
     add "*" symbol before the parameters.
     for non keyword arguments. '''

def multi(*num):
    mul = 2
    for x in num:
          mul *= x
    return mul
print(multi(5, 3, 5))
print(multi(2, 6))

# arbitrary keyword argument.....

''' arbitrary keyword arguments value pass to the function but identified by the key value'''

def fun(**name):
    print(name['name1'])
fun(name1 = "Sandhiya")




