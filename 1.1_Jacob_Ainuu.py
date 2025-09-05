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

#ask for the users name
User_name = str(input("Enter your name"))

#ask for the users age
age = int(input("Enter your age"))


#create an empty list to store push-up results
push_up_result=[]

# Loop 5 times to get 5 push ups results from the users
for i in range(5):
        result = int(input(f"Enter push up result")) # ask for the users push up result
        push_up_result.append(result)                # Display all push up result
        
#----------------Displayimg Results---------------

print("-Push-up result")      # Header for result
print("Result", push_up_result) #  Display all push up result

# calculate the average of the push up result
average = sum(push_up_result) / len(push_up_result)

# Dispplay average, rounded to 2 decimal places
print("average push-ups:", round(average, 2))

# Find and display the highes push up result
best_result = max(push_up_result)
print("Best push-ups results:", best_result)

#-------------Feedback section----------------
# provide feedback based on average performance
print("Feedback")
if average >= 40:
        print("Ecellent Work", User_name + "Your doing well")
elif average >= 25:
        print("Good effort,", User_name + "Keep Training to improve")
else:
        print("Keep going,", User_name + "Practice Makes Perfect")
















