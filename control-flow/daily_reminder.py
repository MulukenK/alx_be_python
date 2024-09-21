variable = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{variable}' is a high priority task that requires immediate attention today!")
        
        else: 
            print(f"Reminder: '{variable}' is a high priority task that you should set the time to do soon.")

    case "medium":
        if time_bound =="yes":
            print(f"Reminder: '{variable}' is a medium priority task that requires immediate attention today!")

        else: 
            print(f"Reminder: '{variable}' is a medium priority task that you should set the time to do soon.")

    case "low":
        
         if time_bound =="yes":
            print(f"Reminder: '{variable}' is a low priority task that requires immediate attention today!")

        else: 
            print(f"Reminder: '{variable}' is a low priority task. Consider completing it when you have free time.")


