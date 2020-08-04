def encrypt(text, s):
    result = ""

    # transverse the plain text
    for i in range(len(text)):
        char = text[i]

        if(char.isspace()):
            result += ' '
            continue
        # encrypt uppercase characters in plain text
        if(char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        # encrypt lowercase characters in plai text
        else:
            result += chr((ord(char) + s-97) % 26 + 97)
        
    return result

    
# check function
text = "CEasER CipHER DemO"
s = 4

print("Plain text: " + text)
print("Shift pattern: " + str(s))
print("Cipher: " + encrypt(text, s))

