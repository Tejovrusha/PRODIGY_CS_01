import string

abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
Abc=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def main():
    while(True):
        print("1. Encryption\n2. Decryption\n3. Exit")
        try:
            x=int(input("Enter your choice: "))
        except Exception:
            print("Enter an integer value")

        if x==1:
            pt=gettxt()
            k=getkey()
            ct=""
            for c in pt:
                if c in abc:
                    j=abc.index(c)
                    ind=(j+k)%26
                    ct+=abc[ind]
                elif c in Abc:
                    j=Abc.index(c)
                    ind=(j+k)%26
                    ct+=Abc[ind]
                else:
                    ct+=c
            
            print("\nCaeser Cipher")
            print(f"Shifted by {k} keys")
            print("Plain Text:",pt)
            print("Cipher Text:",ct)
            print()
            
        elif x==2:
            ct=gettxt()
            k=getkey()
            pt=""
            for c in ct:
                if c in abc:
                    j=abc.index(c)
                    ind=(j-k)%26
                    pt+=abc[ind]
                elif c in Abc:
                    j=Abc.index(c)
                    ind=(j-k)%26
                    pt+=Abc[ind]
                else:
                    pt+=c
            
            print("\nCaeser Cipher")
            print(f"Shifted by {k} keys")
            print("Cipher Text:",ct)
            print("Plain Text:",pt)
            print()
            
        elif x==3:
            break
            
        else:
            print("Enter right choice")
            print()

def gettxt():
    txt=input("Enter a message: ")
    return txt

def getkey():
    while True:
        try:
            k=int(input("Enter a key: "))
            return k
        except Exception:
            print("Enter an integer value")
            continue
        
main()
