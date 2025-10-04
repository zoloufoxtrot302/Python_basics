#variable assignment
x = "python"
print(x)

#variable reassignment 2
x = "python"
y = "is"
z = "awesome"

print(x,y,z)

#multipple variable assignment
a = b = c = "python"
print(a,b,c)

#unpacking a collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#global variable
x = "awesome"   #global variable 
y = "but sometimes tricky"
def myfunc():
  print("Python is " + x)  #accessing global variable inside a function

myfunc()
print("Python is " + y)

#using + operator to combine variables
a = 'hello'
b = ' world'
c = ' I am learining python'
d = ' but it is tricky sometimes'

print(a+b+c+d)

#Global keyword
def myfunc():
  global x
  x = "fantastic"


myfunc()

print("Python is " + x)
print("cpp is also " + x)
print("I am going to learn cloud is it my plan " + x)

#Global keyword 2
x = "awesome 1" #local variable

def myfunc(): 
  global x  #global variable
x = "abracadabra 1"

myfunc()
  
print("Python is " + x)

  #copy paste same code
x = "awesome 2"

def myfunc():
  global x
x = "cool 2"

myfunc()

print("Python is " + x)
  
  
