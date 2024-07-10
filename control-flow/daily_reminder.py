def main():
    # Prompt for a single task
    task = input("Enter your task: ")
    time_bound = input("Is it time-bound (yes or no)? ").lower()
    priority = input("Priority (high, medium, low): ").lower()
    
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