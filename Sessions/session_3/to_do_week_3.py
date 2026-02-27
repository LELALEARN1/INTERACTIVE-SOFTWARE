### USING GUIDANCE STEPS FROM AULA FROM LECTURER'S WAY OF APPROACHING THIS
#Initialise an empty list to store tasks
tasks = []

#Function to add a task to the list
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added to the list")

#Function to view current tasks in the list
def view_tasks():
  print("Current tasks in the list: ")
  if not tasks:
    print("No tasks in the list.")
  else:
    for i, task in enumerate(tasks, 1):
      print(f"{i}. {task}")

#Function to remove a task from the list:
def remove_task(task):
  if task in tasks:
    tasks.remove(task)
    print(f"Task '{task}' removed from the list")
  else:
    print(f"Task '{task}' not found in the list.")

#Main program loop
while True:
  print("\nTo-Do List Manager")
  print("1. Add a task")
  print("2. View tasks")
  print("3. Remove a task")
  print("4. Quit")

  choice = input("Enter your choice: ")
  if choice == "1":
    task = input("Enter a task to add:")
    add_task(task)
  elif choice == "2":
    view_tasks()
  elif choice == "3": # Changed to string comparison
    task = input("Enter a task to remove:")
    remove_task(task)
  elif choice == "4":
    print("Goodbye")
    break
  else:
    print("Invalid choice. Please re-enter.")


