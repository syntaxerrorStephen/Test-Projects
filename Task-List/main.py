def add_task(task_list, task):
  # Add a new task to the task list
  task_list[task] = "pending"
  print(f"Task '{task}' added to the list.")

def view_tasks(task_list):
  # Print all tasks in the task list
  print("\nTasks:")
  for task, status in task_list.items():
    print(f"- {task} ({status})")

def complete_task(task_list, task):
  # Mark a task as completed
  if task in task_list:
    task_list[task] = "completed"
    print(f"Task '{task}' marked as completed.")
  else:
    print(f"Task '{task}' not found.")

def main():
  # Initialize an empty task list
  task_list = {}

  # Prompt the user for a command
  command = input("Enter a command (add, view, complete): ")

  # Execute the command
  if command == "add":
    task = input("Enter a task: ")
    add_task(task_list, task)
  elif command == "view":
    view_tasks(task_list)
  elif command == "complete":
    task = input("Enter a task to mark as completed: ")
    complete_task(task_list, task)
  else:
    print("Invalid command.")

# Run the main function
main()
