# Prompt for a Single Task  
task = input("Enter your task: ")  
priority = input("Priority (high/medium/low): ").strip().lower()  
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()  

# Initialize the reminder message  
reminder = f"'{task}' is a {priority} priority task"  

match priority:  
    case 'high':  
        if time_bound == 'yes':  
            reminder += " that requires immediate attention today!"  
        elif time_bound == 'no':  
            reminder += ". Consider completing it when you have free time."  
    case 'medium':  
        if time_bound == 'yes':  
            reminder += " that requires immediate attention today!"  
        elif time_bound == 'no':  
            reminder += ". Consider completing it when you have free time."  
    case 'low':  
        if time_bound == 'yes':  
            reminder += " that requires immediate attention today!"  
        elif time_bound == 'no':  
            reminder += ". Consider completing it when you have free time."  
    case _:  
        reminder = "Invalid priority level."  

# Provide a Customized Reminder  
print(reminder)
