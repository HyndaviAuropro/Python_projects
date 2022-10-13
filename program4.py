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
        if i['age'] < min_age:  #checks if age of employee is less than min_age or not
            min_age = i['age']  #if age of employee is less than min_age then store the age of employee in "min_age"
            min_emp_name = i['name']  #stores the youngest employee name in " min_emp_name"
    print('name: ', min_emp_name, ' age: ', min_age, )  # prints the name and age of youngest employee
fun(employees) # calling the "fun" function


 #program to print the no of upper case and lower case letters
def myfunc():  #defining "myfun" function
    mystring=input("Enter string:") # Taking userinput
    lower=0 # initializing lower to 0
    upper=0 # initializing upper to 0
    for i in mystring:
        if i.isupper(): #checks if i is upper or not
            upper+=1  # if i is upper, increment upper by 1
        elif i.islower(): #checks if i is lower or not
            lower+=1  # if i is lower, increment lower by 1
        else:
            pass
    print('No of uppercase letters: ',  upper) #printing number of upper case letters
    print('No of lowercase letters: ', lower)  #printing number of lower case letters
myfunc() # calling "myfunc" function


 #program to print even numbers
def even_numbers(): # defining a function with "even numbers"
    num=[1,2,4,5,6,2,5,7,4] # Taking a list
    for i in num:
        if i % 2 == 0: # checks the condition that if i is divided by 2 or not
            print(i) # if i is divided by 2 the i is even number
even_numbers() # calling "even_numbers" function

