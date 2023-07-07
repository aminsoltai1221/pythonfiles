# def Qsay(n,text):
#     pass
n = 20
text = "We can't connect to the server at quera.org. If you entered the      right address, you can:Try again later Check your network connection Check that Firefox has permission to access the web you might be connected but behind a firewall"
words = text.split()
print(words)
while len(words) != 0:
    l = ""
    while len(l) < n:
        if len(words) != 0:
            word = words.pop(0)
            l += word
            if len(words) != 0:
                if len(l + words[0]) > n:
                    print(l)
                    break
                elif len(l + " " + words[0]) == n:
                    word = words.pop(0)
                    l += " " + word
                    print(l)
                    break
                else:
                    l += " "
        