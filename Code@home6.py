# Code@home6_OOP_GUI_Data_Structures
from guizero import App, Box, PushButton, Text, TextBox


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
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
    global stack
    item = input_box.value
    if item:
        stack.push(item)
        input_box.clear()
    stack_text.value = stack.items


def pop_item():
    global stack, popped_item
    popped_item = stack.pop()
    if popped_item is not None:
        pop_text.value = ("Popped item: ", popped_item)
    stack_text.value = stack.items


popped_item = " "
app = App("Stack GUI", width=200, height=200)
stack = Stack()


label = Text(app, text="Stack:")
input_box = TextBox(app)
push_button = PushButton(app, command=push_item, text="Push")
pop_button = PushButton(app, command=pop_item, text="Pop")
pop_text = Text(app, text=("Popped item:", popped_item))
result_text = Text(app, text="")
stack_box = Box(app)
stack_box.bg = "grey"
stack_text = Text(stack_box, text=stack.items)

app.display()
