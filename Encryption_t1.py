alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
to_encrypt=input("Please enter a string to encrypt: ").upper()
shift=int(input("Please enter a digit between 1 and 25 to be your shift: "))
encrypted=""
for char in to_encrypt:
    pos=alphabet.find(char)
    newpos=pos+shift
    if char in alphabet:
        encrypted+=alphabet[newpos]
    else:
        encrypted+=char

print(f"You shifted \"{to_encrypt}\" by {shift} to recieve: {encrypted}")
