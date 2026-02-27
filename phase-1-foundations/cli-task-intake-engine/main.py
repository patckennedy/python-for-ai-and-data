
print('Welcome Guest!')
task = input('Enter a task:').strip()

if not task:
     print("No task entered. Please try again.")
else:
    print(f"Great! One of your tasks for today is : {task}")


