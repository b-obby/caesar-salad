message = 'xf mpwf dbftbs tbmbet' #encrypted text goes here

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

message = message.upper() 
    # for simplicity, this script can only pass through upper case letters. 
    #To bring less burden on the user, the script will automatically convert lower-cased submissions to upper. 

for key in range(len(alphabet)):
    decryption = ''

    for ch in message: 
        if ch in alphabet:
            num = alphabet.find(ch)
            num = num - key
            
            if num <0:
                num = num + len(alphabet)
            decryption = decryption + alphabet[num]

        else:
            decryption = decryption + ch

    print('Attepting Key %s: %s' % (key, decryption))
#the script will attempt every positioning option in a caesarian shuffle. 
#the user combs through all 26 options to find out which result has their deciphered text. 
#The key in the output represents how many positions the plaintext's alphabet was shifted. 