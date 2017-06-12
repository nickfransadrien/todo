import sys
from random import randint
from os.path import expanduser

file_name = expanduser("~") + "/todos.txt"


def load_list(file_name):
    with open(file_name,"r") as f:
        return f.read().splitlines()

def save_list(file_name,lst):
    with open(file_name,"w") as f:
        for item in lst:
            f.write("{}\n".format(item))




class Todos:

    def __init__(self):
        self.lst = load_list(file_name)

    def save(self):
        save_list(file_name, self.lst)
    def add(self,note):
        self.lst.append(note)
    def clear(self):
        self.lst = []
    def random(self):
        print(self.lst[randint(0, len(self.lst)-1)])


    def list(self):
        for index,todo in enumerate(self.lst,1):
            print("{}. {}".format(index,todo))


        
def remove_todos(index):
    pass

def run_interface():
    pass


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
        run_interface()

    todos.save()

main()



