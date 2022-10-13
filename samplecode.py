#######First Program#######

my_list=[1,2,2,4,4,5,6,8,10,13,22,35,52,83]
new_list=[] #Taking a new list
user_input=int(input("Enter number:")) #Taking input from user
for item in my_list:
    if item>=user_input and user_input>=10:
        print(item)
        new_list.append(item) # Appending the item to the new_list
print(new_list) #printing the items in the new_list


output:
Enter number:14
22
35
52
83
[22, 35, 52, 83]

---------------------------------------------------------------------------------------------------------------------------------

##########second code##########

employee={"name": "Tim", "age": 30, "birthday": "1990-03-10", "job": "Devops Engineer"}
del employee["age"] #deleting the age key from the employee list
new_dict={"job":"software engineer"} # Taking a new_dict with "job" key with value as "software engineer"
employee.update(new_dict) # updating the new_dict in employee list
print(employee) #printing the employee list
for item in employee:
    print(item, ':' ,employee[item]) #printing all the items in employee list with key value pairs


 output:
    {'name': 'Tim', 'birthday': '1990-03-10', 'job': 'software engineer'}
name : Tim
birthday : 1990-03-10
job : software engineer
    
-----------------------------------------------------------------------------------------------------------------------------------------------
 ##########Third code###########
 
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
for i in employees: #printing name,job and city of employees in employees list
    print(i['name'] , i['job'] , i['address']['city'] )

print(employees[1]['address']['country'])  #printing the city of the second employee in employees list without looping



output:
 Tina DevOps Engineer New York
 Tim Developer Sydney
 Australia

------------------------------------------------------------------------------------------------------------------------------

##############Fifth code##############(Simple calculator)


def calculation(): #defining a calculator function
    count = 0 # Initializing count to 0
    while True:
        c = input('Enter operation: +,-,*,/,"exit" ')
        if c in ('+','-','*','/','exit') :
            if c == 'exit':
                break
            try:
                 a = int(input('Enter First Number: '))
                 b = int(input('Enter second Numebr: '))

                 count += 1
                 if c == '+':
                    print(a + b)
                 elif c == '-':
                    print(a - b)
                 elif c == '*':
                    print(a * b)
                 elif c == '/':
                     if b == 0 :
                         print("Division with zero is not possible.")
                     else:

                         print(a // b)

            except:
                print('Strings NOT allowed')
        print("calculations:" +str(count))
calculation()

output:
    
Enter operation: +,-,*,/,"exit" /
Enter First Number: 5
Enter second Numebr: 0
Division with zero is not possible.
calculations:1
Enter operation: +,-,*,/,"exit" s
calculations:1
Enter operation: +,-,*,/,"exit" +
Enter First Number: a
Strings NOT allowed
calculations:1
Enter operation: +,-,*,/,"exit" exit
  --------------------------------------------------------------------------------------------------------------------------

###################Sixth program(Guessing Game)##################
import random
def func():

   target_num=random.randint(1,10) #Here target number  range is from 1 to 9 
   guess_num=0 #guess number is initialized to zero
   while target_num!=guess_num:
       try:
           guess_num = int(input("Guess a number:"))
           if guess_num==target_num: #if guessed number is equal to target number the print 'YOU WON'
                print("YOU WON!")
           elif guess_num>target_num: #if guessed number is greater than target number then print guessed number is too high
                print("too high")
           elif guess_num<target_num: #if guessed number is less than target number then print guessed number is too low
                print("too low")
       except:
           print("alphabets not allowed")
func()



output:

Guess a number:1
too low
Guess a number:d
alphabets not allowed
Guess a number:5
too high
Guess a number:4
YOU WON!

