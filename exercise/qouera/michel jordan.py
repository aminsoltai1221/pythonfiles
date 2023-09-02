text = input("please inpur your string : ")
text_reverse = text[::-1]
print(text_reverse)
new_text = ""
for i in range(len(text)):
    if text_reverse[i] == "x":
        new_text = text_reverse[i+1:][::-1] + text_reverse[0:i+1]
        
print(new_text)

    
