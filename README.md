## 📌 Project Description
As part of my Python Development Internship at Codveda Technologies, I developed multiple Python applications to strengthen my programming and problem-solving skills.  

The projects include a **To-Do List Application** for task management and an **API Integration project** that fetches real-time weather data using an external API.  

These projects demonstrate my understanding of Python fundamentals, data structures, file handling, API communication, and real-world application development.

  import json
  import os
  
  FILE_NAME = "tasks.json"
  
  def load_tasks():
      if not os.path.exists(FILE_NAME):
          return []
      try:
          with open(FILE_NAME, "r") as file:
              return json.load(file)
      except json.JSONDecodeError:
          return []
  
  def save_tasks(tasks):
      with open(FILE_NAME, "w") as file:
          json.dump(tasks, file, indent=4)
  
  def add_task(tasks):
      title = input("Enter task title: ")
      tasks.append({"title": title, "completed": False})
      save_tasks(tasks)
      print("Task added successfully!")
  
  def view_tasks(tasks):
      if not tasks:
          print("No tasks available.")
          return
      for index, task in enumerate(tasks, start=1):
          status = "✓" if task["completed"] else "✗"
          print(f"{index}. [{status}] {task['title']}")
  
   def delete_task(tasks):
      view_tasks(tasks)
      try:
          task_num = int(input("Enter task number to delete: "))
          if 1 <= task_num <= len(tasks):
              removed = tasks.pop(task_num - 1)
              save_tasks(tasks)
              print(f"Deleted task: {removed['title']}")
          else:
              print("Invalid task number.")
      except ValueError:
          print("Please enter a valid number.")
   
  def mark_completed(tasks):
      view_tasks(tasks)
      try:
          task_num = int(input("Enter task number to mark as completed: "))
          if 1 <= task_num <= len(tasks):
              tasks[task_num - 1]["completed"] = True
              save_tasks(tasks)
              print("Task marked as completed!")
          else:
              print("Invalid task number.")
      except ValueError:
          print("Please enter a valid number.")
  
  def main():
      tasks = load_tasks()
      
      while True:
          print("\n--- TO-DO LIST MENU ---")
          print("1. Add Task")
          print("2. View Tasks")
          print("3. Delete Task")
          print("4. Mark Task as Completed")
          print("5. Exit")
          
          choice = input("Choose an option: ")
  
          if choice == "1":
              add_task(tasks)
          elif choice == "2":
              view_tasks(tasks)
          elif choice == "3":
              delete_task(tasks)
          elif choice == "4":
              mark_completed(tasks)
          elif choice == "5":
              print("Goodbye!")
              break
          else:
              print("Invalid choice. Try again.")
  
  if __name__ == "__main__":
      main()
