def my_gen():
    n=7
    print("before yield")
    while n<17:
        name = yield 
        print("name is :",name )
        
k = my_gen()
next(k)
k.send("ali")
k.send("ahmad")
k.send("hasan")
k.send("hossain")