# caesar cipher
logo = ''' _____                                  _____  _         _                 
/  __ \                                /  __ \(_)       | |                
| /  \/  __ _   ___  ___   __ _  _ __  | /  \/ _  _ __  | |__    ___  _ __ 
| |     / _` | / _ \/ __| / _` || '__| | |    | || '_ \ | '_ \  / _ \| '__|
| \__/\| (_| ||  __/\__ \| (_| || |    | \__/\| || |_) || | | ||  __/| |   
 \____/ \__,_| \___||___/ \__,_||_|     \____/|_|| .__/ |_| |_| \___||_|   
                                                 | |                       
                                                 |_|                       '''
alphabet = "abcdefghijklmnopqrstuvwxyz"


def lnrsrch(letter):
    for i in range(0, len(alphabet)):
        if (letter == alphabet[i]):
            return i


def encrypt(word, shift):
    alpha = ""
    for j in range(0, len(word)):
        a = lnrsrch(word[j])
        if (a+shift > 25):  # a=25
            alpha += alphabet[(a+shift)-25-1]
        else:
            alpha += alphabet[a+shift]
    print(alpha)


def decrypt(word, shift):
    alpha = ""
    for j in range(0, len(word)):
        a = lnrsrch(word[j])
        if (a-shift < 0):
            alpha += alphabet[a-shift]
        else:
            alpha += alphabet[a-shift]
    print(alpha)


inp3 = "yes"
while (inp3 == "yes" or inp3 == "Yes"):
    print('''Welcome to Caesar Cipher!\n(Encrypted or Decrypted input should be lowercased only)''')
    print(logo)
    inp = int(input("Enter your choice:\n1.Encryption\n2.Decryption\n3.Exit\n"))

    if (inp == 1):
        inp1 = input("Enter the data:")
        inp2 = int(input("Enter the shift amount:"))
        print("Encrypted data is:")
        encrypt(inp1, inp2)
        inp3 = input("Do you want to go back?")
    elif (inp == 2):
        inp1 = input("Enter the data:")
        inp2 = int(input("Enter the shift amount:"))
        print("Decrypted data is:")
        decrypt(inp1, inp2)
        inp3 = input("Do you want to go back?")
    elif (inp == 3):
        exit(0)
    else:
        print("Invalid input!")
