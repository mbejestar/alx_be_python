# Prompt for a Single Task  
task = input("Enter your task: ")  
priority = input("Priority (high/medium/low): ").strip().lower()  
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()  

# Initialize the reminder message  
reminder = f"'{task}' is a {priority} priority task"  

# Determine the urgency based on priority and time sensitivity  
if priority in ['high', 'medium', 'low']:  
    if time_bound == 'yes':  
        reminder += " that requires immediate attention today!"  
    else:  # time_bound is 'no'  
        if priority == 'high':  
            reminder += ". Consider completing it as soon as possible."  
        elif priority == 'medium':  
            reminder += ". Plan to complete it when you can."  
        elif priority == 'low':  
            reminder += ". It can be done at your convenience."  
else:  
    reminder = "Invalid priority level."  

# Provide a Customized Reminder  
print(reminder)
