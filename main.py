from os.path import exists
from os import remove

def task_actions(action):
    tasks = open('tasks.txt', 'r')
    lines = tasks.readlines()
    tasks.close()
    
    count = 0
    
    for line in lines:
        print("{}: {}".format(count, line.strip()))
        count += 1

    selectedTask = int(input("\r\nSelect task to be done by number: \r\n")) 

    if action == "done":
        f = open("done_tasks.txt", "a")
        f.writelines(lines[selectedTask]) 
        f.close() 

        lines.pop(selectedTask)
    
    if action == "removed":
        lines.pop(selectedTask)
    
    if action == "edited":        
        newTaskName = input("Write new name for this task: \r\n")
        lines[selectedTask] = newTaskName

    remove("tasks.txt")

    f = open("tasks.txt", "a")
    for line in lines:
        f.writelines(line) 
    f.close() 

    print("You " + action + " this task successfully")

if not exists("tasks.txt"):  
    open('tasks.txt', 'x').close()    
   
if not exists("done_tasks.txt"):  
    open('done_tasks.txt', 'x').close()   

print("Welcome to simple console based To-do task application!\r\nAvailable options:\r\n")
print("0 - To exit application\r\n1 - Create new task\r\n2 - Show creted tasks\r\n3 - Mark task as done\r\n4 - Remove task\r\n5 - Edit task name")
 
while True:
  selectedTask = int(input("\r\nWrite your option: \r\n")) 

  match selectedTask:
    case 0:
      break
      
    case 1:
      taskName = input("Write name for your new task:\r\n") 

      f = open("tasks.txt", "a")
      f.writelines(taskName + "\n") 
      f.close()

      print("New task has been created:\r\n" + taskName)
      
    case 2:
      f = open("tasks.txt", "r")
      print("\r\nYour task list:\r\n" + f.read()) 
      f.close()
      
    case 3:
      task_actions("done")
      
    case 4:
      task_actions("removed")
      
    case 5:
      task_actions("edited") 
