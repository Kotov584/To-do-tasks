from os.path import exists
from os import remove

def get_tasks():
    tasks = open('tasks.txt', 'r')
    lines = tasks.readlines()
    tasks.close()
    
    count = 0
    
    for line in lines:
        print("{}: {}".format(count, line.strip()))
        count += 1

if not exists("tasks.txt"):  
    open('tasks.txt', 'x').close()    

print("Welcome to simple console based To-do task application!\r\nAvailable options:\r\n")
print("0 - To exit application\r\n1 - Create new task\r\n2 - Show creted tasks\r\n3 - Mark task as done\r\n4 - Remove task\r\n5 - Edit task name")
 
while True:
    selectedTask = int(input("\r\nWrite your option: \r\n")) 
    
    if selectedTask == 0:
        break

    if selectedTask == 1: 
        taskName = input("Write name for your new task:\r\n") 

        f = open("tasks.txt", "a")
        f.writelines(taskName + "\n") 
        f.close()

        print("New task has been created:\r\n" + taskName)

    if selectedTask == 2:
        f = open("tasks.txt", "r")
        print("\r\nYour task list:\r\n" + f.read()) 

    if selectedTask == 3:
        if not exists("done_tasks.txt"):  
            open('done_tasks.txt', 'x').close()   

        get_tasks()

        selectedTask = int(input("\r\nSelect task to be done by number: \r\n")) 

        f = open("done_tasks.txt", "a")
        f.writelines(lines[selectedTask]) 
        f.close() 

        lines.pop(selectedTask)

        remove("tasks.txt")

        for line in lines:
            f = open("tasks.txt", "a")
            f.writelines(line) 
            f.close() 

        print("You done this task successfully")

    if selectedTask == 4:  
        get_tasks()

        selectedTask = int(input("\r\nSelect task to be removed by number: \r\n")) 

        lines.pop(selectedTask)

        remove("tasks.txt")

        for line in lines:
            f = open("tasks.txt", "a")
            f.writelines(line) 
            f.close() 

        print("You removed this task successfully")

    if selectedTask == 5:
        get_tasks()

        selectedTask = int(input("\r\nSelect task to be edited by number: \r\n")) 
        newTaskName = input("Write new name for this task: \r\n")

        lines[selectedTask] = newTaskName

        remove("tasks.txt")

        for line in lines:
            f = open("tasks.txt", "a")
            f.writelines(line) 
            f.close() 

        print("You edited this task successfully")
