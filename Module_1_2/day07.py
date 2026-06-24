#use of parentheses

x= float(input("Enter the value of x: "))

y=1/(x+(1/(x+(1/(x+(1/x))))))

print(y)

# Calculate the end time of an event given a starting time and duration
# Input: Starting time (hours and minutes), Duration (in minutes)
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))


#  Calculate the total minutes from the starting time and duration
total_minutes = hour * 60 + mins + dura

# Calculate the end time in hours and minutes
end_hour = (total_minutes // 60) % 24
end_minute = total_minutes % 60

# Print the end time
print(end_hour, ":", end_minute)


name = input("Enter your name: ")
print("Hello, " + name + ". Nice to meet you!")

print("\nPress Enter to end the program.")
input()
print("THE END.")

num_1 = input("Enter the first number: ") # Enter 12
num_2 = input("Enter the second number: ") # Enter 21

print(num_1 + num_2) # the program returns 1221

my_input = input("Enter something: ") # Example input: hello
print(my_input * 3) # Expected output: hellohellohello