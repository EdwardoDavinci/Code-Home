# Code@home6_OOP_GUI_Data_Structures
from guizero import *

pointer = 0
content = []


def isempty():
    global pointer
    return pointer == 0


def isfull():
    global pointer
    maxsize = 5
    return pointer == maxsize


def push():
    global pointer
    if not isfull():
        content.append(item.value)
        stack.value = content
        item.value = ""
        pointer += 1
        pointerlbl.value = str(pointer)
        error.value = "Pushing"
    else:
        error.value = "Full"


def pop():
    global pointer
    if not isempty():
        content.pop()
        stack.value = content
        pointer -= 1
        pointerlbl.value = str(pointer)
        error.value = "Popping"
    else:
        error.value = "Empty"


app = App(title="Stack", width=200, height=400)
title = Text(app, text="Stack", size=18)
stack = Text(app, text="", width=8, bg="lightsteelblue1")

item = TextBox(app, width=3)
item.focus()

bpush = PushButton(app, text="Push", command=push)
bpop = PushButton(app, text="Pop", command=pop)

pointerlbl = Text(app, text=str(pointer))
error = Text(app, text="")
app.display()
