def main():
    # Prompt for a single task
    task = input("Enter the task description: ")
    priority = input("Enter the task's priority (high, medium, low): ").lower()
    time_bound = input("Is the task time-bound (yes or no)? ").lower()
    
    # Process the task based on priority and time sensitivity
    reminder = ""
    match priority:
        case "high":
            reminder = f"High priority task: {task}."
        case "medium":
            reminder = f"Medium priority task: {task}."
        case "low":
            reminder = f"Low priority task: {task}."
        case _:
            print("Invalid priority level entered. Please enter high, medium, or low.")
            return
    
    # Modify the reminder if the task is time-bound
    if time_bound == "yes":
        reminder += " This task requires immediate attention today!"
    
    # Provide a customized reminder
    print(reminder)

if __name__ == "__main__":
    main()