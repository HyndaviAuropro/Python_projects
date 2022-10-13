#######First Program#######

my_list=[1,2,2,4,4,5,6,8,10,13,22,35,52,83]
new_list=[]
user_input=int(input("Enter number:"))
for item in my_list:
    if item>=user_input and user_input>=10:
        print(item)
        new_list.append(item)
print(new_list)


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
del employee["age"]
new_dict={"job":"software engineer"}
employee.update(new_dict)
print(employee)
for item in employee:
    print(item, ':' ,employee[item])


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
for i in employees:
    print(i['name'] , i['job'] , i['address']['city'] )

print(employees[1]['address']['country'])



output:
 Tina DevOps Engineer New York
 Tim Developer Sydney
 Australia

------------------------------------------------------------------------------------------------------------------------------

##############Fifth code##############(Simple calculator)


try:
    count = 0
    while True:
        a = input('Enter First Number: ')

        if a == 'exit':
            break

        a = int(a)
        b = int(input('Enter second Numebr: '))

        c = input('Enter operation: +,-,*,/ ')
        count += 1
        if c == '+':
            print(a + b)
        elif c == '-':
            print(a - b)
        elif c == '*':
            print(a * b)
        elif c == '/':
            print(a // b)
    print('calculations: ', count)
except:
    print('Division with zero is not possible or Strings NOT allowed')


output:
    
 Enter First Number: 2
Enter second Numebr: 3
Enter operation: +,-,*,/ *
6
Enter First Number: 5
Enter second Numebr: 3
Enter operation: +,-,*,/ -
2
Enter First Number: exit
calculations:  2

  --------------------------------------------------------------------------------------------------------------------------

###################Sixth program(Guessing Game)##################

import random
target_num, guess_num = random.randint(1, 10), 0
while target_num != guess_num:
    guess_num = int(input('Guess a number between : '))
    if guess_num<target_num:
        print("guessed number is too low.")
    elif guess_num>target_num:
        print("guessed number is too high.")
print('YOU WON!')

output:

Guess a number between : 5
guessed number is too high.
Guess a number between : 4
guessed number is too high.
Guess a number between : 3
guessed number is too high.
Guess a number between : 2
YOU WON!
            
