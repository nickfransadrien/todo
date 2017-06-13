import sys
from random import randint
from os.path import expanduser
from os import system

file_name = expanduser("~") + "/todos.txt"


def load_list(file_name):
    with open(file_name,"r") as f:
        return f.read().splitlines()

def save_list(file_name,lst):
    with open(file_name,"w") as f:
        for item in lst:
            f.write("{}\n".format(item))
def getkey():
    pass



class Todos:

    def __init__(self):
        self.lst = load_list(file_name)

    def save(self):
        save_list(file_name, self.lst)
    def add(self,note):
        self.lst.append(note)
    def remove(self,number):
        del self.lst[number]
    def clear(self):
        self.lst = []
    def random(self):
        print(self.lst[randint(0, len(self.lst)-1)])


    def list(self):
        for index,todo in enumerate(self.lst,1):
            print("{}. {}".format(index,todo))


        
def remove_todos(index):
    pass

def run_interface(todos):
    while True:
        system('clear')
        todos.list()
        command = input("Choose an action:")
        if command == "r":
            number = input("Choose a task to remove:")
            todos.remove(int(number)-1)
        if command == "a":
            task = input("Put in new task: ")
            todos.add(task)
        if command == "q":
            break

    


def main():
    
    command = sys.argv[1]
    todos = Todos()



    if command == "list":
        todos.list()
    elif command == "add":
        todos.add(sys.argv[2])
    elif command == "clear":
        todos.clear()
    elif command == "random":
        todos.random()
        
        
    elif command == "interface":
        run_interface(todos)

    todos.save()

main()



