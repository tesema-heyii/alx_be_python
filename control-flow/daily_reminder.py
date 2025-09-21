# daily_reminder.py

# Prompt the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task and provide a customized reminder
match priority:
    case "high":
        if time_bound == "yes":
            print(
                f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(
                f"Reminder: '{task}' is a high priority task. Please complete it as soon as possible.")
    case "medium":
        if time_bound == "yes":
            print(
                f"Reminder: '{task}' is a medium priority task that needs attention today.")
        else:
            print(
                f"Reminder: '{task}' is a medium priority task. Plan to complete it soon.")
    case "low":
        if time_bound == "yes":
            print(
                f"Reminder: '{task}' is a low priority task, but it should be done today.")
        else:
            print(
                f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority. Please enter high, medium, or low.")
