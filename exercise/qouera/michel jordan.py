text = input("please inpur your string : ")
new_text = text 
for i in range(1,len(text)+1):
    i = -1 * i
    if new_text[i] == "x":
        new_text = new_text[:i][::-1] + new_text[i:]     
print(new_text)
