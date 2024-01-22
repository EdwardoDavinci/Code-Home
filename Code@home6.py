# Code@home6_OOP_GUI_Data_Structures
from guizero import App, Box, PushButton, Text


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def size(self):
        return len(self.items)



def push_item():
    item = input_box.value
    if item:
        stack.push(item)
        input_box.clear()

def pop_item():
    popped_item = stack.pop()
    if popped_item is not None:
        print("Popped item:", popped_item)  # You can replace this with a GUI display


app = App("Stack GUI", width=200, height=200)
stack = Stack()


stack_box = Box(app, layout="grid")
label = Text(stack_box, text="Stack:")

input_box = Text(stack_box, text="")
push_button = PushButton(stack_box, command=push_item, text="Push")

pop_button = PushButton(stack_box, command=pop_item, text="Pop")

app.display()