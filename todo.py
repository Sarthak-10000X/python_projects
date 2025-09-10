#sample to do list!(CLI)
todo_list=[]
def show_task():
    if not todo_list:
        print("NO TASK ADDED!")
    else:
        for i, task in enumerate(todo_list,1):
            print(f"{i}. {task}")
        

def add_task(task):
    todo_list.append(task)
    print("TASK ADDED!")

    
def delete_task(idx):
    if 0 < idx < len(todo_list):
        remove= todo_list.pop(idx-1)
        print(f"DELETED: {remove}")
    else:
        print("ENTER A VALID NUMBER!")

while True:
    print("\n===TO DO LIST===")
    print("1. VIEW TASK")
    print("2. ADD TASK")
    print("3. DELETE TASK")
    print("4. EXIT")


    choose=int(input("ENTER NUMBER FROM 1 TO 4: "))



    if choose == 1:
     show_task()
    elif choose == 2:
     task=input("ENTER YOUR TASK: ")
     add_task(task)
    elif choose == 3:
     show_task()
     try:
      idx=int(input("ENTER TASK NUMBER TO DELETE: "))
      delete_task(idx-1)
     except ValueError:
      print("ENTER A VALID NUMBER")

    elif choose == 4:
    
     print("GOODBYE!")
     break             
    else:
     print("INVALID OPTION.")

       
 
     
    


         





    


 

 