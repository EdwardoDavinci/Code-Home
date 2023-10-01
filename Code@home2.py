def is_happy_number(num):
    seen=set()
    while num != 1 and num not in seen:
        seen.add(num)
        num=sum(int(digit)**2 for digit in str(num))
    return num==1

def find_happy_numbers(n):
    happy_numbers=[]
    num=1
    while len(happy_numbers)<n:
        if is_happy_number(num):
            happy_numbers.append(num)
        num+=1
    return happy_numbers

happy_count=int(input("How many happy numbers do you want to find: "))
happy_numbers=find_happy_numbers(happy_count)
print(f"The first {16} happy numbers are: {happy_numbers}")