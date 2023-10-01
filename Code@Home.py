#Code@home1 - Thief
from itertools import permutations
def generate_permutations(number):
    digits = list(str(number))
    permutations_list=["".join(p) for p in permutations(digits)]
    return permutations_list

while True:
    choice=input(f"\nEnter a 3, 4, or 5 digit number or 'q' to quit: ")
    if choice.lower()=='q':
        break
    accountnum=int(choice)
    if 3<=len(str(accountnum))<=5:
        seq=generate_permutations(accountnum)
        print(f"All possible versions of {accountnum}:")
        for permutation in seq:
            print(permutation, end= " ")
    else:
        print("Invalid input. Please enter a 3, 4, or 5 digit number.")