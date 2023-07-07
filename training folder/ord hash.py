data="my name is amin and my pupil number is 9712512148 and number is "
for i in range(10000):
    data=data+str(i)
    data_hash=ord(data)
    if data_hash[-4:]=="1111":
        break
print(data_hash)