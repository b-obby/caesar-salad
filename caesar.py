#Main Encryption Function
def encrypt(input,n):
    result = ""
    
    for i in range(len(input)):
        character = input[i]

        #check for spaces in plaintext and re-add them to the result
        if character==" ":
            result+= " "

        #check for uppercases and encrypt accordingly, as python has different character values for upper vs lower 
        elif (character.isupper()): 
            result += chr((ord(character) + n-65) % 26 + 65)  

        else: 
            result += chr((ord(character) +n-97) % 26 +97) 

    return result

# the user manually enters their plaintext below in the input variable
input = "we love caesar salads" 
# A negative 'n' value will shift the alphabet right (ABC... -> ZAB...) and a positive 'n' value will shift left (ABC... -> BCE...)
n = 1
# Print for the user
print("plaintext is: " + input)
print("Shifting by:" + str(n))
print("Cipher Text is: " + encrypt(input,n)) #parse the above encryption function and print the result