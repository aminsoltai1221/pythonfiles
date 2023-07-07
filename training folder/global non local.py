t=1
def test1():
    a=2
    def test2():
        global t
        t=3
        print("t in test 2 ", t)
    test2()
t=1
def test3():
    a=2
    def test4():
        nonlocal a
        a=3
        print("a in test 4 ", t)
    test4() 
def test5():
    g=2
    print(g ," g in test5")
    def test6():
        def test7():
            nonlocal g
            g=6
            print("g in test7 " , g)
        test7()
    test6()
test1()
test3()
print(t)
test5()