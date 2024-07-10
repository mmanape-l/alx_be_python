# Prompting the user for input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Processing the task based on priority and time sensitivity
print("\nReminder:")
if priority == "high":
    print(f"'{task}' is a high priority task", end=" ")
elif priority == "medium":
    print(f"'{task}' is a medium priority task", end=" ")
elif priority == "low":
    print(f"'{task}' is a low priority task", end=" ")

# Handling time-bound tasks
if time_bound == "yes":
    print("that requires immediate attention today!")
else:
    print("Consider completing it when you have free time.")
