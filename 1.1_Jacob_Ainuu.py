'''

Author: Jacob Ainuu
Date: 25/08/2025
Variation: 1
Describtion: fitness tracker

'''


#-------------------------
#comment first
#input needed - age name and statistics from their fitness
#output needed - greet the user. tell them about the progress and what it will do 

#---------Libaries----------------

User_name = str(input("Enter your name"))
age = int(input("Enter your age"))

push_up_result=[]

for i in range(5):
        result = int(input(f"Enter push up result"))
        push_up_result.append(result)
        
print("Push-up results", push_up_result)













