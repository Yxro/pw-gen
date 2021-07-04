import random
import string
def generator():
    low_alpha = string.ascii_lowercase
#['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    cap_alpha = string.ascii_uppercase
#['Q','W','E','R','T','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
    number = string.digits
#['1','2','3','4','5','6','7','8','9','10']
    special_char = string.punctuation
    end_pw = []
    pw = low_alpha + cap_alpha + number + special_char
    #print(pw)
#=for y in pw:
   # op = print(y, end="")

#for n in pw:
    #print(n, end="")

#for x in pw:
    #print(x, end="")
#print(pw_character)


    pw_len = int(input("\nhow many characters whould you like your password to include: "))
    print("your new generated password is")

#random_num = random.choices(pw)
    i = 0
    pw_len += 1
#print(pw_len)
    while i < pw_len:
        i += 1
        if i < pw_len:
            u = random.choice(pw)
            end_pw.append(u)
            print(u, end="")

wlcm = input("Hi there, would you like to start generating passwords? (Y)\(N): ")
if wlcm.capitalize() == "Y":
    generator()
    answer = input("\nwould you like to keep restarting the process? (Y)\(N): ")
    if answer.capitalize() == 'Y':
        while answer.capitalize() == 'Y':
            generator()
    else:
        pass


