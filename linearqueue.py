def menu():
    print("""
    1. Add
    2. Remove
    3. Is empty
    4. Is full?""")


def emptycheck(size):
    if size == 0:
        return False
    else:
        return True


def fullcheck(size, maxsize):
    if size == maxsize:
        return False
    else:
        return True


front = 0
rear = -1
size = 0
maxsize = 5

queue = [ ]
while True:
    menu()
    choice = input("What do you choose? ")
    if choice=="1":
            if fullcheck(size, maxsize):
                newelement = input("What would you like to add to your queue: ").lower()
                queue.append(newelement)
                rear += 1
                size += 1
                print(f"front:{front},rear:{rear},size:{size}")
            else:
                print("queue full")
    elif choice=="2":
            for i in queue:
                print(i, ",", end=" ")
            xelement = input("What would you like to remove from the queue: ")
            queue.remove(xelement)