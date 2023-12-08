#caesersays-Task1
def encryptor(text, shift):
    result=""
    for char in text:
        if char.isalpha():
            offset=ord("a") if char.islower() else ord("A")
            result+=chr((ord(char)-offset+shift)%26+offset)
        else:
            result+=char
    return result

def decryptor(text, shift):
    result=""
    for char in text:
        if char.isalpha():
            offset=ord("a") if char.islower() else ord("A")
            result+=chr((ord(char)-offset-shift)%26+offset)
        else:
            result+=char
    return result

text=input("What would you like to encrypt: ")
shift=int(input("What would you like to shift by: "))
encrypted=encryptor(text, shift)
print(f"Encrypted: {encrypted}")
decrypted=decryptor(encrypted, shift)
print(f"Decrypted: {decrypted}")
