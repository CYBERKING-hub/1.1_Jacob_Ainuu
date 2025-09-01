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
        
print("-Push-up result")
print("Result", push_up_result)

average = sum(push_up_result) / len(push_up_result)
print("average push-ups:", round(average, 2))

best_result = max(push_up_result)
print("Best push-ups results:", best_result)

print("Feedback")
if average >= 40:
        print("Ecellent Work", User_name + "Your doing well")
elif average >= 25:
        print("Good effort,", User_name + "Keep Training to improve")
else:
        print("Keep going,", User_name + "Practice Makes Perfect")
















