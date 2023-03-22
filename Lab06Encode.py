#Kian Ambrose
#add commen

def encode(string):
    d = []
    for i in string:
        a= int(i)
        if a<7:
            b = a+3
        else:
            b = a-7
        b= str(b)
        d.append(b)
    str1=""
    for j in d:
        str1 += j
    return str1


if __name__ == "__main__":

    while True:
        print("Menu")
        print("-"*13)
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        x = input("Please enter an option: ")

        c = input("Please enter your password to encode: ")





        if x== "1":
            encode(c)

            print("Your password has been encoded and stored!")

        elif x == "2":
            pass

        elif x == "3":
            break



