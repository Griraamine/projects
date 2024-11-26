import json
import argparse


parser=argparse.ArgumentParser(description="your to-do list")
parser.add_argument("command",choices=["add","update","list","exit","delete","update_status"],help="add your action")
parser.add_argument("--task",help="your task name")
parser.add_argument("status",choices=["done","in_progess","undone"],help="your task's status")
args=parser.parse_args()
Tasks={}
try:
    with open("tasks.json","r") as file:
        Tasks=json.load(file)
except FileNotFoundError:
    Tasks={}



def save_to_file():
    with open("tasks.json", "w")as file:
        json.dump(Tasks,file,indent=4)





def add(task):
    if not task:print("error! dakhel task");return
    elif task in Tasks:print(f"{task} already exists")
    else: Tasks[task]="undone";print("task added successfully")


def listing():
    if not Tasks:print("list is empty")
    else:
        for i,(key,value) in enumerate(Tasks.items(),start=1):
                print(f"{i} : {key} -- {value}")


def update(old_task,new_task):
    if not old_task or not new_task:print("ti het tasks");return
    elif old_task not in Tasks:print("Invalid task")
    else:
        Tasks[new_task]=Tasks.pop(old_task)

def update_status(task,status):
    if not task or not status:print("yezi mel bleda");return
    elif task not in Tasks:print("mouch  golet lik yezi mel bleda")
    else:
        Tasks[task]=status


def delete(task):
    if not task:print("errrrrrrrrrrreeeuur");return
    elif task not in Tasks:print("invalid task")
    else:del Tasks[task]




if __name__=="__main__":
    if args.command=="add":
        add(args.task)
        save_to_file()
    elif args.command=="list":
        listing()
    elif args.command=="update":
        update(args.task,input("ur new task"))
        save_to_file()
    elif args.command=="update_status":
        update_status(args.task,args.status)
        save_to_file()
    elif args.command=="delete":
        delete(args.task)
        save_to_file()
    elif args.command=="exit":
        save_to_file()
        exit()

