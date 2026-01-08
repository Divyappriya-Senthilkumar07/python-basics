# print basic statements 
print('hi')


print('Good Morning!')
print("It is a rainy today")


print('Good Morning!', end=' ')
print("It is a rainy today")

#print using import

import keyword
print(keyword.kwlist)


#check for variables 
var1 = 'John'
print(var1)

var1 = 'Sam'
print(var1)
var1 = 'Matt'
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



# getting the input as string 

name = input('Enter your Name : ')
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
print('Name1 : ', name1)
print('Name2 : ', name2)
print('Name3 : ', name3)


#giving multiple values and also using split 
name1, name2, name3 = input('Enter 3 names: ').split(',')
print('Name1 : ', name1)
print('Name2 : ', name2)
print('Name3 : ', name3)


#generating a month and year 

import calendar
year = int(input('Enter the year as number:'))
month = int(input('Enter the month as number:'))
print(calendar.month(year,month))

#using a string 
s = "Life iS beautifuL !!! "
print("Life" in s)
print("Fast" in s)


s = "Life iS beaUtiful !!! "
print(s.count('!'))


s = "Life iS beaUtifulf"
print(s.endswith('l'))


s = "Life iS beaUtiful"
print(s.find("b"))


s = "Life iS beaUtiful"
print(s.replace('f','v'))

a = 'life is beautiful'
b = ' live happily'
print(a,b)
print(a + b)


#string formatting 

#using the curly brackets
print('{} and {} are best friends'.format('Ram','Sam'))


#using the positional arguements
print('{0} and {1} are best friends'.format('Ram','Sam'))
print('{1} and {0} are best friends'.format('Ram','Sam'))


# using keyword arguements
print('{a},{b},{c}'.format(a='James',b='peter',c='Rocky'))


#code 

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))



#code 
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))