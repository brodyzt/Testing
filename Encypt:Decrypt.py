dec_char = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','.',',',' ','0','1','2','3','4','5','6','7','8','9']
enc_char = [' ','b','8','e','k','5','x','i','.','v','r','4','t','j','9','z','p',',','m','n','6','d','1','h','2','l','u','q','o','w','0','y','f','s','7','c','3','g','a']
enc_char2 = [' ','b','8','1','5','k','i','x','q','e','r','y','t','f','z','9','p',',','g','n','6','d','v','h','l','2','u','.','o','w','4','0','j','s','c','7','3','m','a']

def decrypted_string(enc_string):
    temp_string = ''
    for x in range(len(enc_string)):
        char = enc_string[x]
        if(char in enc_char):
            if(x % 2 == 0):
                temp_string = temp_string + dec_char[enc_char.index(char)]
            else:
                temp_string = temp_string + dec_char[enc_char2.index(char)]
        else:
            temp_string = temp_string + char
    return temp_string
def encrypted_string(dec_string):
    temp_string = ''
    for x in range(len(dec_string)):
        char = dec_string[x]
        if(char in dec_char):
            if(x % 2 == 0):
                temp_string = temp_string + enc_char[dec_char.index(char)]
            else:
                temp_string = temp_string + enc_char2[dec_char.index(char)]
        else:
            temp_string = temp_string + char
    return temp_string

choice = input('Would you like to encrypt a message or decrypt a message?\n1.Encrypt\n2.Decrypt\n\nChoice: ')

if(choice == '1'):
    text = input('Please enter the text to encrypt: ').lower()
    print('The encrypted text is: ' + encrypted_string(text))
else:
    text = input('Please enter the text to decrypt: ').lower()
    print('The decrypted text is: ' + decrypted_string(text))
