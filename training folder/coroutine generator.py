def splitor(delimiter = " "):
    string = ""
    result = []
    word = ""
    c = 0
    while True:
        for i in string:
            if i == delimiter:
                result.append(word)
                word = ""
            word += i
            if c == len(string)-1:
                result.append(word)
            c += 1
        string = yield result
                
            
g = splitor()
next(g)
print(g.send("ali hasan hossain"))
