#Code@home4.5 Base Conversion
from time import sleep
hexcode=["1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
def dec_to_bin(dec):
    if dec==0:
        return 0
    bin=""
    while dec>0:
        remainder=dec%2
        bin=str(remainder)+bin
        dec//=2
    return bin
def bin_to_dec(bin):
    dec=0
    multiplier=1
    for i in range(len(bin)-1,-1,-1):
        if bin[i]=="1":
            dec+=1*multiplier
        multiplier*=2
    return dec

def dec_to_hex(dec):
    hex=""
    while dec>0:
        remainder = dec % 16
        if remainder<=10:
            hex=str(remainder)+hex
        elif remainder==10:
            hex="A"+hex
        elif remainder==11:
            hex="B"+hex
        elif remainder==12:
            hex="C"+hex
        elif remainder==13:
            hex="D"+hex
        elif remainder==14:
            hex="E"+hex
        elif remainder==15:
            hex="F"+hex
        dec=dec//16
    return hex
def hex_to_dec(hex_val):
    dec = 0
    multiplier = 1
    for i in range(len(hex_val)-1, -1, -1):
        hex_digit = hex_val[i]
        if hex_digit.isdigit():
            dec += int(hex_digit) * multiplier
        else:
            dec += (hexcode.index(hex_digit)+1) * multiplier
        multiplier *= 16
    return dec
def bin_to_hex(binnum):
    decnum=bin_to_dec(binnum)
    hexnum=dec_to_hex(decnum)
    return hexnum
def hex_to_bin(hexnum):
    decnum = hex_to_dec(hexnum)
    binnum = dec_to_bin(decnum)
    return binnum
def menu():print("""
1. Base 10 to Base 2
2. Base 2 to Base 10
3. Base 10 to Base 16
4. Base 16 to Base 10
5. Base 2 to Base 16
6. Base 16 to Base 2
7.Quit""")
while True:
    sleep(1)
    menu()
    choice=input("Which do you choose ")
    if choice=="1":
        decnum=int(input("Which base 10 number do you choose "))
        binnum=dec_to_bin(decnum)
        print(f"{decnum} written in base 2 is {binnum}")
    elif choice=="2":
        binnum = input("Which base 2 number do you choose ")
        decnum = bin_to_dec(binnum)
        print(f"{binnum} written in base 10 is {decnum}")
    elif choice=="3":
        decnum = int(input("Which base 10 number do you choose "))
        hexnum = dec_to_hex(decnum)
        print(f"{decnum} written in base 16 is {hexnum}")
    elif choice=="4":
        hexnum = (input("Which base 16 number do you choose "))
        decnum = hex_to_dec(hexnum)
        print(f"{hexnum} written in base 10 is {decnum}")
    elif choice=="5":
        binnum = input("Which base 2 number do you choose ")
        hexnum = bin_to_hex(binnum)
        print(f"{binnum} written in base 16 is {hexnum}")
    elif choice=="6":
        hexnum = input("Which base 16 number do you choose ")
        binnum = hex_to_bin(hexnum)
        print(f"{hexnum} written in base 2 is {binnum}")
    else:
        break
