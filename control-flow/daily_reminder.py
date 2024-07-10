# Prompting the user for input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Printing the initial reminder message format
print(f"Reminder: '{task}' is a", end=" ")

# Handling the priority with if-elif statements
if priority == "high":
    print("high priority task", end=" ")
elif priority == "medium":
    print("medium priority task", end=" ")
elif priority == "low":
    print("low priority task", end=" ")
else:
    print("task with unknown priority", end=" ")

# Handling time-bound tasks
if time_bound == "yes":
    print("that requires immediate attention today!")
else:
    print("Consider completing it when you have free time.")
