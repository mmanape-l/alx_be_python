# Prompting the user for input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Processing the task based on priority and time sensitivity
print("\nReminder:")

# Using match statement for priority
match priority:
    case "high":
        print(f"'{task}' is a high priority task", end=" ")
    case "medium":
        print(f"'{task}' is a medium priority task", end=" ")
    case "low":
        print(f"'{task}' is a low priority task", end=" ")
    case _:
        print(f"'{task}' has an unknown priority", end=" ")

# Handling time-bound tasks
if time_bound == "yes":
    print("that requires immediate attention today!")
else:
    print("Consider completing it when you have free time.")
