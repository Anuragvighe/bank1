def acc(name,city,uid,psw,bal):
    fp=open("E:\\python\\name.txt",'w')
    fp.write(name)
    fp.close()

    fp = open("E:\\python\\city.txt", 'w')
    fp.write(city)
    fp.close()

    fp = open("E:\\python\\uid.txt", 'w')
    fp.write(uid)
    fp.close()

    fp = open("E:\\python\\psw.txt", 'w')
    fp.write(psw)
    fp.close()

    fp = open("E:\\python\\bal.txt", 'w')
    fp.write(bal)
    fp.close()

if __name__ == '__main__':
    name=input("Enter a name:")
    city=input("Enter a city:")
    uid=input("Enter a uid")
    psw=input("Enter a psw")
    bal=input("Enter a bal")
    acc(name,city,uid,psw,bal)
    print("Acc Open successfully !!!")
