# print basic statements 
print('hi')


print('Good Morning!')
print("It is a sunny today")


print('Good Morning!', end=' ')
print("It is a sunny today")

#print using import

import keyword
print(keyword.kwlist)


#check for variables 
var1 = 'Aaron'
print(var1)

var1 = 'Kenji'
print(var1)
var1 = 'Juliette'
print(var1)


# check for data type
a = 10
type(a)

a = 10.5
type(a)

a = 'Sneha'
type(a)

a = True
type(a)


#square root of a number 
num = float(input("Enter a number: "))
sqrt = num ** 0.5
print("Square root =", sqrt)



#cube root of a number
num = float(input("Enter a number: "))
cuberoot = num ** (1/3)
print("Cube root =", cuberoot)


#area of a circle 
radius = float(input("Enter the radius: "))
area = 3.14159 * radius * radius
print("Area of the circle =", area)



# getting the input as string 

name = input('Enter your Name:')
print('hi ',name)


# getting integer as input statement

a = int(input('Enter the value of A: '))
print(type(a))
b = int(input('Enter the value of B: '))
print(type(b))
c = a+b
print(c)


#getting the input as float 
a = float(input('Enter the value for A  : '))
b = float(input('Enter the value for B : '))
c = a+b
print(c)


#giving multiple values 
name1, name2, name3 = input('Enter 3 names: ').split()
print('Name1: ', name1)
print('Name2: ', name2)
print('Name3: ', name3)


#giving multiple values and also using split 
name1, name2, name3 = input('Enter 3 names: ').split(',')
print('Name1: ', name1)
print('Name2: ', name2)
print('Name3: ', name3)


#generating a month and year 

import calendar
year = int(input('Enter the year as number:'))
month = int(input('Enter the month as number:'))
print(calendar.month(year,month))

#using a string 
s = "Life is beautifuL !!! "
print("Life" in s)
print("Fast" in s)


s = "Life is beautiful !!! "
print(s.count('!'))


s = "Life is beautiful"
print(s.endswith('l'))


s = "Life is beautiful"
print(s.find("b"))


s = "Life is beautiful"
print(s.replace('f','i'))

a = 'life is beautiful'
b = ' live the best'
print(a,b)
print(a + b)


#string formatting 

#using the curly brackets
print('{} and {} are good friends'.format('Aaron','Kenji'))


#using the positional arguements
print('{0} and {1} are best friends'.format('Aaron','Kenji'))
print('{1} and {0} are best friends'.format('Aaron','Kenji'))


# using keyword arguements
print('{a},{b},{c}'.format(a='James',b='castle',c='Aaron'))


#code 

quantity = 5
itemno = 101
price = 50.51
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))



#code 
age = 19
txt = "My name is Aaron, and I am {}"
print(txt.format(age))


#even or odd code
num = int(input('Enter the number: '))
if(num%2 == 0):
  print('It is Even')
else:
  print('It is odd')



  #find the biggest of three numbers
a = int(input('Enter A : '))
b = int(input('Enter B : '))
c = int(input('Enter C : '))

if(a>b and a>c):

  print('A is the biggest number')
if(b>a and b>c):

  print('B is the biggest number')
if(c>a and c>b):

  print('C is the biggest number')



#checking the eligibilty for voting

print("Check if the person is eligible to vote or not")
age=int(input("Enter your Age: "))


if age<18:
    print("Not eligible to Vote")
else:
    print("You are eligible to vote")


#guessing a number
print("Guess a Number: ")
num = input()
num = int(num)

if num>10 and num<20:
    print("Correct Guess!")
else:
    print("Incorrect Guess!")


#reg code
regno = int(input("Enter Register no : "))
if regno in [101,102,103,110]:
    print("pass")
else:
    print("Fail")



    