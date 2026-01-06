

def print_list():
  for i in range(len(todolist)):
    print(str(i) + ": " + todolist[i])

def write_list():
  f = open("list.txt", "w")
  for i in todolist[0:-2]:
    f.write(i+"\n")
  f.write(todolist[-1])
  f.close()



f = open("list.txt", "r")
todolist = f.read().splitlines()
f.close()

print_list()

while True:
  
  user_input = input("Would you like to add a task, remove a task, or quit?")
  
  if user_input == "remove" or user_input == "remove a task":
    remove_choice = input("Type the number of the item you would like to remove")
    todolist.pop(int(remove_choice))
    write_list()
  elif user_input == "add" or user_input == "add a task":
    add_choice = input("What task would you like to add?")
    todolist.append(add_choice)
    write_list()
  elif user_input == "quit":
    exit()

  print_list()
