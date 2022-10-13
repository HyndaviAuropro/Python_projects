employees = [{
  "name": "Tina",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer",
  "address": {
    "city": "New York",
    "country": "USA"
  }
},
{
  "name": "Tim",
  "age": 35,
  "birthday": "1985-02-21",
  "job": "Developer",
  "address": {
    "city": "Sydney",
    "country": "Australia"
  }
}]

def fun(employees):   #printing out the name and age of youngest employee
    min_age = 1000000000000
    min_emp_name = ''

    for i in employees:
        if i['age'] < min_age:
            min_age = i['age']
            min_emp_name = i['name']
    print('name: ', min_emp_name, ' age: ', min_age, )
fun(employees)

def myfunc():  #printing the no of upper case and lower case letters
    mystring=input("Enter string:")
    lower=0
    upper=0
    for i in mystring:
        if i.isupper():
            upper+=1
        elif i.islower():
            lower+=1
        else:
            pass
    print('No of uppercase letters: ',  upper)
    print('No of lowercase letters: ', lower)
myfunc()

def even_numbers(): #printing even numbers
    num=[1,2,4,5,6,2,5,7,4]
    for i in num:
        if i % 2 == 0:
            print(i)
even_numbers()

