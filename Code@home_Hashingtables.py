from random import randint
import matplotlib.pyplot as plt
import numpy as np

def generate_random_numbers(num):
    numlist=[]
    for i in range(num):
        numlist.append(randint(1,10000))
    return numlist
def create_hash_table(size):
    hash_table=[None]*size
    return hash_table

def hash_function(num, size):
    return num % size

def insert_into_hash_table(table, num, size):
    global collisions
    index=num%size
    while table[index]!=None:
        index+=1
        collisions+=1
        if index==size:
            index=0
    table[index]=num


collisions=0
collisioncount=[]
random_numbers = generate_random_numbers(1000)


table_sizes=[]
for i in range(1000,10000,10):
    table_sizes.append(i)
    hash_table = create_hash_table(i)
    collisions = 0
    for num in random_numbers:
        insert_into_hash_table(hash_table, num, i)
        if None not in hash_table:
            print("table is full")
            break
    collisioncount.append(collisions)
    print(f"Table size: {i}, Collisions: {collisions}")

x = np.array(table_sizes)
y = np.array(collisioncount)

plt.plot(x, y, "o")

plt.xlabel("table size")
plt.ylabel("collision count")

plt.show()
