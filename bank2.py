def withdraw():
    bal=int(input("Enter a Amount to be Withdraw: "))
    fp=open("E:\\python\\bal.txt",'r')
    bal1=int(fp.read())
    fp.close()
    if(bal<=bal1):
        print("withdraw successful")
        bal1=bal1-bal
        print("Remaining amt: ",bal1)
        fp = open("E:\\python\\bal.txt", 'w')
        fp.write(str(bal1))
    else:
        print("withdraw unsuccessful")

def deposit():
    bal = int(input("Enter a Amount to be Deposit: "))
    fp = open("E:\\python\\bal.txt", 'r')
    bal1 = int(fp.read())
    fp.close()
    bal1=bal1+bal
    print("\n Current Amt: ",bal1)
    fp = open("E:\\python\\bal.txt", 'w')
    fp.write(str(bal1))
    fp.close()

def bal_chk():
    fp = open("E:\\python\\bal.txt", 'r')
    bal1 = int(fp.read())
    fp.close()
    print("Your current balance is: ",bal1)

def change():
    print("1.Change the login ID")
    print("2.Change the Password")
    k=int(input("\n Please Enter valid option: "))
    if k==2:
        p=input("please Enter a New Password: ")
        fp=open("E:\\python\\psw.txt",'w')
        fp.write(str(p))
        fp.close()
        print("Password Change successfully ")

    elif k==1:
        p = input("please Enter a New ID: ")
        fp = open("E:\\python\\uid.txt", 'w')
        fp.write(str(p))
        fp.close()
        print("Login ID Change successfully ")
    else:
        print("Given option is incorrect \n please Enter a valid option")


def uid_psw(u,p):
    fp=open("E:\\python\\uid.txt",'r')
    uid1=fp.read()
    fp.close()
    fp=open("E:\\python\\psw.txt",'r')
    psw1=fp.read()
    fp.close()
    if u == uid1 and p == psw1:
        print("login successfully\n")
        fp=open("E:\\python\\name.txt",'r')
        n=fp.read()
        print("How Can I Help You Mr.",n)
        print("1.withdraw: ")
        print("2.Deposit: ")
        print("3.balance check: ")
        print("4.change password or Login Id :\n")

        o=int(input("Enter a Valid option: "))
        if(o==1):
            withdraw()
        elif(o==2):
            deposit()
        elif(o==3):
            bal_chk()
        elif(o==4):
            change()
        else:
            print("Given option is incorrect \n please Enter a valid option")


    else:
        print("enter valid information")



if __name__ == '__main__':
    u=input("Enter a login ID: ")
    p=input("Enter a Password: ")
    uid_psw(u,p)
