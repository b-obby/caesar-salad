message = 'this is our encrypted caesar message'

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(alphabet)):
    decryption = ''

    for ch in message: 
        if ch in alphabet:
            num = num - key
            
            if num <0:
                num = num + len(alphabet)
            decryption = decryption + alphabet[num]

        else:
            decryption = decryption + ch

    print('Brute Force Key is %s: %s'(key, decryption))

