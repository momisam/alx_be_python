# daily_reminder.py
# A very simple program to remind you of one task

# Step 1: Ask the user for details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Step 2: Check the priority using match case
match priority:
    case "high":
        message = "Reminder: '" + task + "' is a high priority task"
    case "medium":
        message = "Reminder: '" + task + "' is a medium priority task"
    case "low":
        message = "Note: '" + task + "' is a low priority task. Consider completing it when you have free time."
    case _:
        message = "Invalid priority entered."

# Step 3: If the priority was valid, check if it is time-bound
if priority == "high" or priority == "medium" or priority == "low":
    if time_bound == "yes":
        message = message + " that requires immediate attention today!"

# Step 4: Show the reminder
print(message)