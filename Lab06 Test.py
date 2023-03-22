#Kian Ambrose
# Neil Patel is making this edit
def encoder(string):
    d = []
    for i in string:
        a = int(i)
        if a < 7:
            b = a + 3
        else:
            b = a - 7
        b = str(b)
        d.append(b)
    str1 = ""
    for j in d:
        str1 += j
    return str1


def decoder(fake_p):
    fake_p = list(fake_p)
    string2 = ""
    for i in range(len(fake_p)):
        if fake_p[i] == "0":
            fake_p[i] = "7"
            string2 += fake_p[i]
            continue
        if fake_p[i] == "2":
            fake_p[i] = "9"
            string2 += fake_p[i]
            continue
        if fake_p[i] == "1":
            fake_p[i] = "8"
            string2 += fake_p[i]
            continue
        if fake_p[i] == "3" or fake_p[i] == "4" or fake_p[i] == "5" or fake_p[i] == "6" or fake_p[i] == "7" or fake_p[i] == "8" or fake_p[i] == "9":
            real = (int(fake_p[i]) - 3)
            string2 += str(real)
    return string2


if __name__ == "__main__":

    while True:
        print("Menu")
        print("-"*13)
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        x = input("\nPlease enter an option: ")

        if x == "1":
            c = input("Please enter your password to encode: ")
            store_fake = encoder(c)
            print("Your password has been encoded and stored!\n")
        elif x == "2":
            print(f"The encoded password is {store_fake}, and the original password is {decoder(store_fake)}.\n")
        elif x == "3":
            break