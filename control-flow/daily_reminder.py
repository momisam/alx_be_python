# daily_reminder.py
# A simple program that gives you a reminder about one task

# Step 1: Ask the user for details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Step 2: Use match case to handle priority
match priority:
    case "high":
        if time_bound == "yes":
            print("Reminder: '" + task + "' is a high priority task that requires immediate attention today!")
        else:
            print("Reminder: '" + task + "' is a high priority task")
    case "medium":
        if time_bound == "yes":
            print("Reminder: '" + task + "' is a medium priority task that requires immediate attention today!")
        else:
            print("Reminder: '" + task + "' is a medium priority task")
    case "low":
        if time_bound == "yes":
            print("Reminder: '" + task + "' is a low priority task that requires immediate attention today!")
        else:
            print("Reminder: '" + task + "' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Reminder: Invalid priority entered.")