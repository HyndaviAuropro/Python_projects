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
    while True:
        num1 = input('Enter First Number: ')

        if num1 == 'exit':
            break

        num1 = int(num1)
        num2 = int(input('Enter second Numebr: '))

        num3 = input('Enter operation: +,-,*,/ ')

        if num3 == '+':
            print(num1 + num2)
        elif num3 == '-':
            print(num1-num2)
        elif num3 == '*':
            print(num1*num2)
        elif num3 == '/':
            print(num1 // num2)

except:
    print('Division with zero is not possible or Strings NOT allowed')
        


output:
    
    Enter First Number: 11
Enter second Numebr: 22
Enter operation: +,-,*,/ +
33
Enter First Number: 1
Enter second Numebr: 3
Enter operation: +,-,*,/ *
3
Enter First Number: 5
Enter second Numebr: 4
Enter operation: +,-,*,/ /
1
Enter First Number: 1
Enter second Numebr: 2
Enter operation: +,-,*,/ /
0
Enter First Number: 5
Enter second Numebr: 0
Enter operation: +,-,*,/ /
Division with zero is not possible or Strings NOT allowed

  --------------------------------------------------------------------------------------------------------------------------
            
