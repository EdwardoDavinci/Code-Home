#code@home2p2
def encryptor(text, keyword):
    result=""
    for char in text:
        if char.isalpha():
            result+=chr((ord(char)-ord("a")+ord(keyword[text.index(char)%len(keyword)])-ord("a"))%26+ord("a"))
        else:
            result+=char
    return result
def decryptor(text, keyword):
    result=""
    for i in range(len(text)):
        pos=i
        char=text[i]
        if char.isalpha():
            result+= chr(((ord(char)-ord("a") - (ord(keyword[pos%len(keyword)]) - ord("a"))%26)%26 + ord("a")))
        else:
            result+=char
    return result
text="the quick brown fox jumped over the lazy dog".lower()
keyword="abcde"
print(encryptor(text, keyword))
print(decryptor(encryptor(text, keyword), keyword))
