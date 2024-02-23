# Code@home10 Mcnugget numbers

def mcnugget_check(n):
    if n < 0:
        return False
    if n == 0:
        return True
    for i in range(n // 20 + 1):
        for j in range(n // 9 + 1):
            for k in range(n // 6 + 1):
                if i * 20 + j * 9 + k * 6 == n:
                    return True
    return False

def find_all_mcnuggets():
    mcnuggets=[]
    non_mcnuggets=[]
    for i in range(1,100):
        if mcnugget_check(i):
            mcnuggets.append(i)
        else:
            non_mcnuggets.append(i)
    return mcnuggets, non_mcnuggets

mcnuggets, non_mcnuggets = find_all_mcnuggets()
print(f"All the mcnugget numbers are {mcnuggets}")
print(f"All the non mcnugget numbers are {non_mcnuggets}")
