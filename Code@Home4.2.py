#Code@home 4 task 2 - midsquare hashing
from random import randint, choice

def generate_random_numbers(num):
    numlist=[]
    for i in range(num):
        numlist.append(randint(1000,99999999))
    return numlist
def create_hashtable(num):
    hashtable=[None]*int((num*1.7))
    return hashtable

def hash_function(num):
    squared=num**2
    squared=str(squared)
    middle_index = len(squared)//2
    hashed_value = int(squared[middle_index-1:middle_index+1])
    return hashed_value

def insert_into_hash_table(table,num):
    index=hash_function(num)
    while table[index]!=None:
        index+=1
        if index==100:
            index=0
    table[index]=num
    return table
def find_num(table,num):
    index=hash_function(num)
    while table[index]!=num:
        index+=1
    if table[index]==num:
        print(f"{num} found at posistion {index}")


randomnums=generate_random_numbers(100)
table=create_hashtable(100)
for num in randomnums:
    hash_table=insert_into_hash_table(table,num)
    if None not in hash_table:
        print("table is full")
        break
rannum=choice(randomnums)
print(hash_table)
print(hash_function(rannum))
find_num(hash_table,rannum)


