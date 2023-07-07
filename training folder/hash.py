import hashlib
import random
while True:
    data="my name is amin and my pupil's number is 9712512148"
    def upper_creator(string):
        situations=random.sample([i for i in range(41)],random.randint(0,10))
        strlist=[i for i in string]
        for i in situations:
            try:
                Uppercase=string[i].upper()
                strlist[i]=Uppercase
            except:
                pass
        newstring="".join(strlist)
        return newstring
    # print(upper_creator(data))
    m=hashlib.sha256()
    m.update(upper_creator(data).encode("utf-8"))
    hashh=m.hexdigest()
    if hashh[-4:]=="0000":
        break
print(hashh)
print(upper_creator(data))