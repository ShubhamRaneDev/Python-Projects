distance = int(input("What is the distance you walked (km) : "))
time = int(input("How much time did it take you to reach your destination (minutes) : "))
speed = (distance/time)
question = input("Would you like to calculate the speed ? :")
if question == "Yes": print("Your average speed was", speed)
if question == "No": print("Fine I won't print it.")