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

#this is a list, list always start counting from 0
Workout_result_list = ["Push ups", "Pull ups", "Running", "Squats", "Jumping Jacks"]

    print(Workout_result_list) #prints every students

count = 0 #creating a count
while count<len(Workout_result_list):
    print(count, Workout_result_list[count])
    count+=5
print("This are all the results")

print(Workout_result_list[0]) 
print(Workout_result_list[1])
print(Workout_result_list[2])
print(Workout_result_list[3])
print(Workout_result_list[4])


      








